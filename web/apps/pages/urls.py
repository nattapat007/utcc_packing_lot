from django.urls import path

from .views import HomePageView, DetectPageView, CheckinPageView, CheckoutPageView
from ..parking.views import ParkingExportView

app_name = 'page'

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('detect/', DetectPageView.as_view(), name='detect'),
    path('checkin/', CheckinPageView.as_view(), name='checkin'),
    path('checkout/', CheckoutPageView.as_view(), name='checkout'),
    path('export/', ParkingExportView.as_view(), name='export'),
]
