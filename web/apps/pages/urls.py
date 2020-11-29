from django.urls import path
from .views import HomePageView, DetectPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('detect/', DetectPageView.as_view(), name='detect'),
]
