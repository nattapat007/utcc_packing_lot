from django.conf.urls import url
from django.urls import path

from .views import SignupPageView, LoginPageView, logout_view, UserProfileUpdateView

urlpatterns = [
    path("signup/", SignupPageView.as_view(), name="signup"),
    url('login/$', LoginPageView.as_view(), name='login'),
    url('logout/$', logout_view, name='logout'),
    url(r'^update/(?P<pk>\d+)/$', UserProfileUpdateView.as_view(), name='update'),
]
