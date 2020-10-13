from django.contrib import admin

# Register your models here.
from web.apps.commons.admin import SoftModelControllerAdmin
from web.apps.parking.models import Park


@admin.register(Park)
class ParkAdmin(SoftModelControllerAdmin):
    list_display = ('user', 'motorcycle')
    search_fields = ('user', 'motorcycle')