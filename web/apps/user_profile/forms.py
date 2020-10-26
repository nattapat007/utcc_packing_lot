from crispy_forms.bootstrap import PrependedText
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from django import forms
from django.contrib.auth import authenticate, login
from django.utils.translation import ugettext_lazy as _
from model_controller.forms import ModelControllerForm

from web.apps.commons.forms import BaseForm
from web.apps.commons.utils import EXCLUDE_COMMON_FIELDS
from web.apps.user_profile.models import UserProfile
from web.apps.motorcycle.models import Brand, Model

from django.contrib.auth.models import User


class UserProfileAdminForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = '__all__'


class UserProfileCreationForm(forms.ModelForm):
    username = forms.CharField(max_length=50, min_length=3, initial='')
    password = forms.CharField(widget=forms.PasswordInput(), initial='')
    email = forms.EmailField(required=True)
    family_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    phone = forms.CharField(min_length=10, max_length=10)
    image = forms.ImageField(label=_('Image'), required=False)
    brand = forms.ModelChoiceField(queryset=Brand.objects.all(), required=True, empty_label="Other")
    model = forms.ModelChoiceField(queryset=Model.objects.all(), required=True, empty_label="Other")
    color = forms.CharField(required=True)

    def __init__(self, *args, **kwargs):
        super(UserProfileCreationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            'username',
            'password',
            'email',
            'family_name',
            'last_name',
            'phone',
            'image',
            'brand',
            'model',
            'color'
        )
        self.helper.add_input(Submit('submit', _('Sign Up'), css_class='btn btn-success'))

    class Meta:
        model = UserProfile
        exclude = EXCLUDE_COMMON_FIELDS + ('user',)


class LoginForm(BaseForm):
    username = forms.CharField(required=True)
    password = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)
        self.helper.form_method = 'POST'
        self.helper.form_show_labels = False
        self.helper.layout = Layout(
            PrependedText('username', '<i class="fa fa-user"></i>', placeholder='Username'),
            PrependedText('password', '<i class="fa fa-lock"></i>', placeholder='Password'),
            Submit('login', 'Log In', css_class='btn btn-success')
        )

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)

        if not user or not user.is_active:
            raise forms.ValidationError(_('Invalid Username or Password'))

        return self.cleaned_data

    def login(self, request):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)

        if user and user.is_active:
            login(request, user)


class UserProfileUpdateForm(forms.ModelForm):
    family_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    phone = forms.CharField(min_length=10, max_length=10)
    image = forms.ImageField(label=_('Image'), required=False)
    brand = forms.ModelChoiceField(queryset=Brand.objects.all(), required=True, empty_label="Other")
    model = forms.ModelChoiceField(queryset=Model.objects.all(), required=True, empty_label="Other")
    color = forms.CharField()

    def __init__(self, *args, **kwargs):
        super(UserProfileUpdateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            'family_name',
            'last_name',
            'phone',
            'image',
            'brand',
            'model',
            'color',
        )
        self.helper.add_input(Submit('submit', _('Update'), css_class='btn btn-success'))

    class Meta:
        model = UserProfile
        exclude = EXCLUDE_COMMON_FIELDS + ('user',)
