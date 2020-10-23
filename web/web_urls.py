from django.urls import path, include

urlpatterns = [
    path('', include('web.apps.pages.urls')),
    path('user_profile/', include('web.apps.user_profile.urls')),
]
