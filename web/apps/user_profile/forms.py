from django import forms

from web.apps.user_profile.models import UserProfile


class UserProfileAdminForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = '__all__'