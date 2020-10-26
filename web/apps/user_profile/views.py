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
from web.apps.motorcycle.models import Motorcycle


class SignupPageView(generic.CreateView):
    form_class = UserProfileCreationForm
    success_url = reverse_lazy("login")
    template_name = "signup.html"

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        brand = request.POST.get('brand')
        model = request.POST.get('model')
        color = request.POST.get('color')
        is_active = False

        user = User.objects.create_user(username=username, password=password, email=email, is_active=is_active)
        motor = Motorcycle.objects.create(brand=brand, model=model, color=color, )

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


class UserProfileUpdateView(generic.UpdateView):
    model = UserProfile
    success_url = reverse_lazy("home")
    template_name = "edit_profile.html"
    form_class = UserProfileUpdateForm

    def post(self, request, *args, **kwargs):
        user_profile = UserProfile.objects.get(pk=kwargs['pk'])

        user_profile.family_name = request.POST.get('family_name')
        user_profile.last_name = request.POST.get('last_name')
        user_profile.phone_number = request.POST.get('phone')
        user_profile.image = request.FILES.get('image')

        user_profile.save()
        return redirect(self.success_url)


def logout_view(request):
    logout(request)
    response = redirect(reverse_lazy('login'))
    return response


def verify_view(request):
    users_false = UserProfile.objects.filter(user__is_active=False)
    return render(request, 'user_verify.html', {'users_false': users_false})


def verify_update(request, pk):
    user = User.objects.get(pk=pk)
    print(user)
    if request.method == "POST":
        for i in user:
            i.is_active = True
            i.save()
    else:
        print(user.is_active, pk)

    return redirect('user_verify')
