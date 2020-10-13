from django.urls import path, include

urlpatterns = [
    path('', include('web.apps.authentications.urls'), name='home'),
    # path('user_profile/', include('web.apps.user_profile.urls'), name='user_profile')
]
