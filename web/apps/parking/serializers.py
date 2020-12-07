import datetime

import pytz
from django.http import HttpResponse
from openpyxl import Workbook
from rest_framework import serializers

from web.apps.commons.choices import InOutStatus
from web.apps.motorcycle.serializers import MotorcycleSerializer
from web.apps.parking.models import Park


def excel_file_response(prefix_filename: str, workbook: Workbook) -> HttpResponse:
    response = HttpResponse(content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
    current_datetime = datetime.datetime.now().strftime('%Y%m%d_%H%M%s')
    file_name = f'{prefix_filename}_{current_datetime}'
    response['Content-Disposition'] = f'attachment; filename={file_name}.xlsx'
    workbook.save(response)
    return response


class ParkSerializer(serializers.ModelSerializer):
    motorcycle = MotorcycleSerializer(read_only=True)
    status = serializers.SerializerMethodField()

    class Meta:
        model = Park
        fields = ['motorcycle', 'created_at', 'updated_at', 'status']

    def get_status(self, obj):
        '''
        Show choice
        https://docs.djangoproject.com/en/3.1/ref/models/instances/#django.db.models.Model.get_FOO_display
        '''
        return obj.get_status_display()


class ParkExportSerializer:
    class Meta:
        model = Park
        fields = '__all__'

    def __init__(self, **kwargs):
        self.start_date = kwargs.get('start_date')
        self.end_date = kwargs.get('end_date')
        self.start_date = self.start_date.replace(
            hour=0, minute=0, second=0, tzinfo=pytz.UTC
        )
        self.end_date = self.end_date.replace(
            hour=23, minute=59, second=59, tzinfo=pytz.UTC
        )
        print(f'StartDate: {self.start_date}, EndDate: {self.end_date}')

        self.model_class = self.Meta.model
        self.fields = self.Meta.fields

        self.workbook = Workbook()
        self.worksheet = self.workbook.active
        self.queryset = self.get_query_set()

        header = self.get_header()
        self.worksheet.append(header)
        self.export_operation()
        self.response = excel_file_response('park', self.workbook)

    def get_query_set(self):
        return Park.objects.select_related('user', 'motorcycle').filter(
            created_at__range=(self.start_date, self.end_date))

    def get_header(self):
        header = [
            'ลำดับ', 'ทะเบียน', 'ชื่อ', 'สกุล', 'ว/ด/ป เวลาเข้า', 'ว/ด/ป เวลาออก', 'ระยะเวลาที่จอด'
        ]
        return header

    def export_operation(self):
        sequence = 0
        for index, park in enumerate(self.queryset):
            sequence = index + 1
            create_at = park.created_at.strftime('%d/%m/ %X')
            update_at = park.updated_at.strftime('%d/%m/ %X')
            check_in_date = f'{create_at[:6]}{park.created_at.year + 543}{create_at[6:]} น.'
            check_out_date = f'{update_at[:6]}{park.updated_at.year + 543}{update_at[6:]} น.'

            park_created_at = park.created_at.replace(second=0, microsecond=0)
            park_updated_at = park.updated_at.replace(second=0, microsecond=0)
            find_time = park_updated_at - park_created_at if park.status == InOutStatus.CHECKOUT else ''
            if find_time != '':
                if find_time.seconds < 3600:
                    find_time = f'{str(find_time).split(":")[1]} นาที'
                else:
                    find_time = f'{".".join(str(find_time).split(":")[:2])} ชั่วโมง'

            data = [
                sequence,
                park.motorcycle.plate,
                park.user.family_name,
                park.user.last_name,
                check_in_date,
                check_out_date if park.status == InOutStatus.CHECKOUT else 'ยังไม่ได้ Check out',
                find_time
            ]
            self.worksheet.append(data)
        self.get_footer(sequence)

    def get_footer(self, sequence):
        footers = [
            ['', '', '', '', '', '', ''],
            ['', '', '', '', '', '', ''],
            ['สรุป', f'{sequence} ที่เข้าจอด', '', '', '', '', '']
        ]
        for footer in footers:
            self.worksheet.append(footer)
