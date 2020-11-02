from django.conf.urls import url
from django.urls import path

from .views import SignupPageView, LoginPageView, logout_view, UserProfileUpdateView, verify_view, verify_update, \
    UserMultipleUploadImagesView

urlpatterns = [
    path("signup/", SignupPageView.as_view(), name="signup"),
    url('login/$', LoginPageView.as_view(), name='login'),
    url('logout/$', logout_view, name='logout'),
    url(r'^update/(?P<pk>\d+)/$', UserProfileUpdateView.as_view(), name='update'),
    url(r'^multiple_image_upload/(?P<pk>\d+)/$', UserMultipleUploadImagesView.as_view(), name='multiple_image_upload'),

    path("user_verify/", verify_view, name="user_verify"),
    path("verify/<str:pk>/", verify_update, name="verify"),
]
