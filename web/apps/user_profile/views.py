# Create your views here.
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import TemplateView
from django.views.generic.edit import BaseFormView

from web.apps.user_profile.forms import CustomUserCreationForm, LoginForm
from web.apps.user_profile.models import UserProfile


class SignupPageView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "signup.html"

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')

        user = User.objects.create_user(username=username, password=password, email=email)

        data = {
            'user': user,
            'created_user': user,
            'updated_user': user,
            'family_name': request.POST.get('family_name'),
            'last_name': request.POST.get('last_name'),
            'phone_number': request.POST.get('phone'),
            'image': request.FILES.get('image')
        }

        UserProfile.objects.create(**data)
        return redirect(self.success_url)


class LoginPageView(TemplateView, BaseFormView):
    template_name = "login.html"
    success_url = reverse_lazy('home')
    form_class = LoginForm

    def form_valid(self, form):
        form.login(self.request)
        return super(LoginPageView, self).form_valid(form)


class ProfilePageView(generic.UpdateView):
    model = UserProfile
    fields = ["first_name"]
    success_url = reverse_lazy("home")
    template_name = "profile.html"


def logout_view(request):
    logout(request)
    response = redirect(reverse_lazy('login'))
    return response
