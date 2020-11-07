from rest_framework import routers

from web.apps.checkinout.views import CheckInViewSet, CheckOutViewSet

router = routers.DefaultRouter()
app_name = 'api_urls'

# API URL should be sorted by name
# Ex. router.register(r'users', UserViewSet, base_name='users')
router.register(r'checkin', CheckInViewSet, basename='checkin')
router.register(r'checkout', CheckOutViewSet, basename='checkout')

urlpatterns = [

]

urlpatterns += router.urls