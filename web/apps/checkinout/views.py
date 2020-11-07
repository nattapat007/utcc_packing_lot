from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from web.apps.checkinout.serializers import CheckInSerializer, CheckOutSerializer
from web.apps.parking.models import Park


class CheckInViewSet(viewsets.ModelViewSet):
    queryset = Park.objects.all()
    serializer_class = CheckInSerializer
    permission_classes = (AllowAny,)


class CheckOutViewSet(viewsets.ModelViewSet):
    queryset = Park.objects.all()
    serializer_class = CheckOutSerializer
    permission_classes = (AllowAny,)
