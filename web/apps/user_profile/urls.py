from django.conf.urls import url
from django.urls import path

from .views import SignupPageView, ProfilePageView, LoginPageView, logout_view

urlpatterns = [
    path("signup/", SignupPageView.as_view(), name="signup"),
    url('login/$', LoginPageView.as_view(), name='login'),
    url('logout/$', logout_view, name='logout'),
    path("<int:pk>/profile/", ProfilePageView.as_view(), name="profile"),
]
