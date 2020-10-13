from rest_framework import routers

router = routers.DefaultRouter()
app_name = 'api_urls'

# API URL should be sorted by name
# Ex. router.register(r'users', UserViewSet, base_name='users')