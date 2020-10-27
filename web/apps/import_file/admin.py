from django.contrib import admin
# Register your models here.
from openpyxl import load_workbook

from web.apps.commons.admin import SoftModelControllerAdmin
from web.apps.import_file.brand_model_import import brand_model_import
from web.apps.import_file.models import ImportFile


@admin.register(ImportFile)
class ImportFileAdmin(SoftModelControllerAdmin):
    list_display = ('created_at', 'file')

    def save_model(self, request, obj, form, change):
        file = form.files.get('file')
        workbook = load_workbook(file, data_only=True)
        worksheet = workbook.worksheets[0]
        user = request.user

        import_result_data = {
            'file': file,
            'created_user': user,
            'updated_user': user
        }
        ImportFile.objects.create(**import_result_data)
        brand_model_import(worksheet, user)
        super().save_model(request, obj, form, change)
