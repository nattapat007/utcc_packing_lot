from django.urls import path, include

from web.apps.parking.export_park import export_park_xls

urlpatterns = [
    path('', include('web.apps.pages.urls')),
    path('user_profile/', include('web.apps.user_profile.urls')),
    path('export/park/', export_park_xls, name='export_park_xls'),
]
