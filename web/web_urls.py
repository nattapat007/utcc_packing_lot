from django.urls import path, include

urlpatterns = [
    path('', include('web.apps.pages.urls', namespace='home')),
    path('user_profile/', include('web.apps.user_profile.urls', namespace='user_profile')),
    path('page/', include('web.apps.pages.urls', namespace='page')),
]
