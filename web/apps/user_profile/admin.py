from django.contrib import admin

# Register your models here.
from model_controller.admins import ModelControllerAdmin

from web.apps.user_profile.forms import UserProfileAdminForm
from web.apps.user_profile.models import UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(ModelControllerAdmin):
    list_display = ('user', 'family_name', 'last_name', 'phone_number')
    search_fields = ('id', 'user__username', 'family_name', 'last_name')
    list_filter = ('id', 'created_at', 'updated_at')
    form = UserProfileAdminForm