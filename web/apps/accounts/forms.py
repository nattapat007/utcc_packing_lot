from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm
from django.utils.translation import ugettext_lazy as _

from web.apps.commons.utils import EXCLUDE_COMMON_FIELDS
from web.apps.user_profile.models import UserProfile


class CustomUserCreationForm(forms.ModelForm):
    username = forms.CharField(max_length=50, min_length=3, initial='')
    password = forms.CharField(widget=forms.PasswordInput(), initial='')
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    phone = forms.CharField(min_length=10, max_length=10)
    image = forms.ImageField(label=_('Image'), required=False)

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            'username',
            'password',
            'email',
            'family_name',
            'last_name',
            'phone',
            'image'
        )
        self.helper.add_input(Submit('submit', _('Sign Up'), css_class='btn btn-success'))

    class Meta:
        model = UserProfile
        exclude = EXCLUDE_COMMON_FIELDS + ('user',)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = (
            "email",
            "username",
        )
