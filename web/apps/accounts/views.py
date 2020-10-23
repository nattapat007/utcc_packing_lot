# Create your views here.
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic

from web.apps.accounts.forms import CustomUserCreationForm
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


class ProfilePageView(generic.UpdateView):
    model = UserProfile
    fields = ["first_name"]
    success_url = reverse_lazy("home")
    template_name = "profile.html"
