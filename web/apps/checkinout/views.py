import logging
from datetime import datetime

import face_recognition
import numpy as np
from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from web.apps.checkinout.models import CheckIn, CheckOut
from web.apps.checkinout.serializers import CheckInSerializer, CheckOutSerializer
from web.apps.commons.choices import InOutStatus
from web.apps.parking.models import Park
from web.apps.user_profile.models import UserProfile

log = logging.getLogger(__name__)


def find_matches_image_between_user(basename, query_data):
    user_profiles = UserProfile.objects.all()

    know_face_id = []
    know_face_encodings = []

    for user_profile in user_profiles.values('id', 'image'):
        know_face_id.append(user_profile['id'])
        know_face_encodings.append(
            face_recognition.face_encodings(face_recognition.load_image_file('/code/media/' + user_profile['image']),
                                            model='cnn')[0])

    unknown_image = face_recognition.load_image_file(query_data)
    face_locations = face_recognition.face_locations(unknown_image)
    face_encodings = face_recognition.face_encodings(unknown_image)

    if not face_locations or not face_encodings:
        return '', "Can't find face locations or face_encoding"

    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        matches = face_recognition.compare_faces(know_face_encodings, face_encoding)

        face_distances = face_recognition.face_distance(know_face_encodings, face_encoding)
        best_match_index = np.argmin(face_distances)

        if matches[best_match_index]:
            user_id = know_face_id[best_match_index]

            user_profile = user_profiles.filter(user_id=user_id)

            if basename == 'checkin':
                create_check_in_out = CheckIn.objects.create(face_login=query_data)

                Park.objects.create(
                    user=user_profile,
                    motorcycle='',
                    status=InOutStatus.CHECKIN,
                    checkin=create_check_in_out,
                    created_user=user_profile,
                )
            elif basename == 'checkout':
                create_check_in_out = CheckIn.objects.create(face_login=query_data)

                now = datetime.now()
                start_date = now.replace(hour=0, minute=0, second=0)
                end_date = now.replace(hour=23, minute=59, second=59)

                park = Park.objects.filter(user=user_profile,
                                           created_at__range=(start_date, end_date),
                                           status=InOutStatus.CHECKIN,
                                           checkin__isnull=False,
                                           checkout__isnull=True)

                park.status = InOutStatus.CHECKOUT
                park.checkout = create_check_in_out
                park.updated_user = user_profile
                park.save()

            log.info(f'{user_profile}, {create_check_in_out}')
            return user_profile, create_check_in_out
        else:
            log.info('Unknown')
            return 'Unknown', None


class CheckInViewSet(viewsets.ModelViewSet):
    queryset = CheckIn.objects.all()
    serializer_class = CheckInSerializer
    permission_classes = (AllowAny,)

    def create(self, request, *args, **kwargs):
        user_profile, check_in = find_matches_image_between_user(self.basename, request.data['face_login'])

        if check_in == "Can't find face locations or face_encoding":
            return Response(data=check_in, status=status.HTTP_404_NOT_FOUND)

        data = CheckInSerializer(check_in).data
        return Response(data=data, status=status.HTTP_200_OK)


class CheckOutViewSet(viewsets.ModelViewSet):
    queryset = CheckOut.objects.all()
    serializer_class = CheckOutSerializer
    permission_classes = (AllowAny,)

    def create(self, request, *args, **kwargs):
        user_profile, check_out = find_matches_image_between_user(self.basename, request.data['face_logout'])

        if check_out == "Can't find face locations or face_encoding":
            return Response(data=check_out, status=status.HTTP_404_NOT_FOUND)

        data = CheckOutSerializer(check_out).data
        return Response(data=data, status=status.HTTP_200_OK)
