from django.contrib import admin

# Register your models here.
from web.apps.commons.admin import SoftModelControllerAdmin
from web.apps.motorcycle.models import Brand, Model, Motorcycle


@admin.register(Brand)
class BrandAdmin(SoftModelControllerAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name', )


@admin.register(Model)
class ModelAdmin(SoftModelControllerAdmin):
    list_display = ('brand', 'model_name')
    search_fields = ('model_name', )


@admin.register(Motorcycle)
class MotorcycleAdmin(SoftModelControllerAdmin):
    list_display = ('brand', 'model', 'color', 'plate')
    search_fields = ('brand', 'model', 'color', 'plate')
