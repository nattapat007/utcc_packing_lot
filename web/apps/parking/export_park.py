from datetime import datetime

from django.http import HttpResponse
from openpyxl import Workbook

from web.apps.commons.choices import InOutStatus
from web.apps.parking.models import Park


def export_park_xls(request):
    response = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
    )
    response['Content-Disposition'] = 'attachment; filename={date}-park.xlsx'.format(
        date=datetime.now().strftime('%Y-%m-%d'),
    )

    parks = Park.objects.select_related('motorcycle')
    book = Workbook()
    sheet = book.active
    header = [
        'วันที่', 'เลขทะเบียน', 'เวลาเข้า', 'เวลาออก', 'ระยะเวลาที่จอด'
    ]

    sheet.append(header)
    for park in parks:
        park_created_at = park.created_at.replace(second=0, microsecond=0)
        park_updated_at = park.updated_at.replace(second=0, microsecond=0)

        find_time = (park_updated_at - park_created_at
                     if (park_updated_at != park_created_at or park_updated_at == park_created_at) and
                        park.status == InOutStatus.CHECKOUT else '')

        data = [
            park.created_at.strftime('%d %B %Y'),
            park.motorcycle.plate,
            park.created_at.strftime('%X'),
            park.updated_at.strftime('%X') if park.status == InOutStatus.CHECKOUT else '',
            find_time
        ]
        sheet.append(data)

    book.save(response)

    return response
