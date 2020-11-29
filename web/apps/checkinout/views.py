from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from web.apps.checkinout.face_recognition import find_matches_image_between_user
from web.apps.checkinout.models import CheckIn, CheckOut
from web.apps.checkinout.serializers import CheckInSerializer, CheckOutSerializer


class CheckInViewSet(viewsets.ModelViewSet):
    queryset = CheckIn.objects.prefetch_related('park_set', 'park_set__motorcycle')
    serializer_class = CheckInSerializer
    permission_classes = (AllowAny,)

    def create(self, request, *args, **kwargs):
        user_profile, check_in = find_matches_image_between_user(self.basename, request.data['face_login'],
                                                                 request.data['plate'])

        if check_in == "Can't find face locations or face_encoding":
            return Response(data=check_in, status=status.HTTP_404_NOT_FOUND)

        data = CheckInSerializer(check_in).data
        return Response(data=data, status=status.HTTP_200_OK)


class CheckOutViewSet(viewsets.ModelViewSet):
    queryset = CheckOut.objects.prefetch_related('park_set', 'park_set__motorcycle')
    serializer_class = CheckOutSerializer
    permission_classes = (AllowAny,)

    def create(self, request, *args, **kwargs):
        user_profile, check_out = find_matches_image_between_user(self.basename, request.data['face_logout'],
                                                                  self.request.POST['plate'])

        if check_out == "Can't find face locations or face_encoding":
            return Response(data=check_out, status=status.HTTP_404_NOT_FOUND)

        data = CheckOutSerializer(check_out).data
        return Response(data=data, status=status.HTTP_200_OK)
