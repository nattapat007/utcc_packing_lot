from django.urls import path

from web.apps.authentications.views import HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home')
]