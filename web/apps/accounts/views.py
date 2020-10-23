# Create your views here.
from django.urls import reverse_lazy
from django.views import generic

from web.apps.accounts.forms import CustomUserCreationForm
from web.apps.user_profile.models import UserProfile


class SignupPageView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "signup.html"


class ProfilePageView(generic.UpdateView):
    model = UserProfile
    fields = ["first_name"]
    success_url = reverse_lazy("home")
    template_name = "profile.html"
