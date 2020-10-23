from django.urls import path, include

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('web.apps.accounts.urls')),
    path('', include('web.apps.pages.urls')),
]
