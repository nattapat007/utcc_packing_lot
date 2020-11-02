# Create your views here.
import logging

from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import TemplateView
from django.views.generic.edit import BaseFormView

from web.apps.motorcycle.models import Motorcycle, Brand, Model
from web.apps.user_profile.forms import UserProfileCreationForm, LoginForm, UserProfileUpdateForm, \
    UserMultipleUploadImagesForm
from web.apps.user_profile.models import UserProfile, UserMultipleImages

logger = logging.getLogger('django')


class SignupPageView(generic.CreateView):
    form_class = UserProfileCreationForm
    success_url = reverse_lazy("login")
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
        user_profile.image = request.FILES.get('image') if request.FILES.get(
            'image') != '' else user_profile.image

        user_profile.save()
        return redirect(self.success_url)


def logout_view(request):
    logout(request)
    response = redirect(reverse_lazy('login'))
    return response


def verify_view(request):
    users_false = Motorcycle.objects.filter(profile__user__is_active=False, profile__user__is_superuser=False)
    return render(request, 'user_verify.html', {'users_false': users_false})


def verify_update(request, pk):
    user = User.objects.get(pk=pk)
    logger.info(f'User: {user}')
    if request.method == "POST":
        user.is_active = True
        user.save()
    else:
        logger.info(f'ID: {pk} active {user.is_active}')

    return redirect('user_verify')


class UserMultipleUploadImagesView(generic.CreateView):
    form_class = UserMultipleUploadImagesForm
    success_url = reverse_lazy("home")
    template_name = "multiple_upload.html"

    def post(self, request, *args, **kwargs):
        user = User.objects.get(pk=request.user.id)
        user_profile = UserProfile.objects.get(pk=kwargs.get('pk'))

        image_bulk_create = []
        image_list = request.FILES.getlist('image')
        for image in image_list:
            image_bulk_create.append(
                UserMultipleImages(image=image,
                                   user_profile=user_profile,
                                   created_user=user,
                                   updated_user=user
                                   )
            )
        UserMultipleImages.objects.bulk_create(image_bulk_create)
        return redirect(self.success_url)
