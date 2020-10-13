from django.contrib import admin

# Register your models here.
from web.apps.commons.admin import SoftModelControllerAdmin
from web.apps.import_file.models import ImportFile


@admin.register(ImportFile)
class ImportFileAdmin(SoftModelControllerAdmin):
    list_display = ('created_at', 'file')
