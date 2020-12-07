# Create your views here.
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import TemplateView
from django.views.generic.edit import BaseFormView

from web.apps.user_profile.forms import UserProfileCreationForm, LoginForm, UserProfileUpdateForm
from web.apps.user_profile.models import UserProfile
from web.apps.motorcycle.models import Motorcycle, Brand, Model


class SignupPageView(generic.CreateView):
    form_class = UserProfileCreationForm
    success_url = reverse_lazy("user_profile:login")
    template_name = "signup.html"

    def post(self, request, *args, **kwargs):
        user_data = {
            'username': request.POST.get('username'),
            'password': request.POST.get('password'),
            'email': request.POST.get('email'),
            'is_active': False
        }
        user = User.objects.create_user(**user_data)

        profile_data = {
            'user': user,
            'created_user': user,
            'updated_user': user,
            'family_name': request.POST.get('family_name'),
            'last_name': request.POST.get('last_name'),
            'phone_number': request.POST.get('phone'),
            'image': request.FILES.get('image'),
        }
        user_profile = UserProfile.objects.create(**profile_data)

        brand = Brand.objects.get(pk=request.POST.get('brand'))
        model = Model.objects.get(pk=request.POST.get('model'))

        motorcycle_data = {
            'profile': user_profile,
            'brand': brand,
            'model': model,
            'color': request.POST.get('color'),
            'plate': request.POST.get('plate'),
            'created_user': user,
            'updated_user': user,
        }
        Motorcycle.objects.create(**motorcycle_data)

        return redirect(self.success_url)


class LoginPageView(TemplateView, BaseFormView):
    template_name = "login.html"
    success_url = reverse_lazy('home:home')
    form_class = LoginForm

    def form_valid(self, form):
        form.login(self.request)
        return super(LoginPageView, self).form_valid(form)


class UserProfileUpdateView(generic.UpdateView):
    model = UserProfile
    success_url = reverse_lazy("home:home")
    template_name = "edit_profile.html"
    form_class = UserProfileUpdateForm

    def post(self, request, *args, **kwargs):
        user_profile = UserProfile.objects.get(pk=kwargs['pk'])
        user_profile.family_name = request.POST.get('family_name')
        user_profile.last_name = request.POST.get('last_name')
        user_profile.phone_number = request.POST.get('phone')
        user_profile.image = request.FILES.get('image') if request.FILES.get(
            'image') != '' else user_profile.image

        user_profile.save()
        return redirect(self.success_url)


def logout_view(request):
    logout(request)
    response = redirect(reverse_lazy('user_profile:login'))
    return response


def verify_view(request):
    users_false = Motorcycle.objects.filter(profile__user__is_active=False, profile__user__is_superuser=False)
    return render(request, 'user_verify.html', {'users_false': users_false})


def verify_update(request, pk):
    users = User.objects.filter(pk=pk)
    print(users)
    if request.method == "POST":
        for user in users:
            user.is_active = True
            user.save()
    else:
        print(users.is_active, pk)

    return redirect('user_verify')
