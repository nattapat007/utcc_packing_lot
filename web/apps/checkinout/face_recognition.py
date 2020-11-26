import base64
import logging
from datetime import datetime
from io import BytesIO

import face_recognition
import numpy as np
from django.core.files.base import ContentFile

from web.apps.checkinout.models import CheckIn, CheckOut
from web.apps.commons.choices import InOutStatus
from web.apps.motorcycle.models import Motorcycle
from web.apps.parking.models import Park
from web.apps.user_profile.models import UserProfile

log = logging.getLogger(__name__)


def find_matches_image_between_user(basename, image, plate):
    user_profiles = UserProfile.objects.all()

    know_face_id = []
    know_face_encodings = []

    for user_profile in user_profiles.values('id', 'image'):
        know_face_id.append(user_profile['id'])
        know_face_encodings.append(
            face_recognition.face_encodings(face_recognition.load_image_file('/code/media/' + user_profile['image']),
                                            model='cnn')[0])

    bytes_image = BytesIO(base64.b64decode(image))
    unknown_image = face_recognition.load_image_file(bytes_image)
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

            user_profile = user_profiles.get(user_id=user_id)
            motorcycle = Motorcycle.objects.get(plate=plate)

            if basename == 'checkin' and user_profile.id == motorcycle.profile_id:
                image_file = ContentFile(base64.b64decode(image), 'checkin.jpg')
                create_check_in_out = CheckIn.objects.create(face_login=image_file, plate=plate)

                Park.objects.create(
                    user=user_profile,
                    motorcycle=motorcycle,
                    status=InOutStatus.CHECKIN,
                    checkin=create_check_in_out,
                    created_user=user_profile.user,
                    updated_user=user_profile.user
                )

            elif basename == 'checkout' and user_profile.id == motorcycle.profile_id:
                image_file = ContentFile(base64.b64decode(image), 'checkin.jpg')
                create_check_in_out = CheckOut.objects.create(face_logout=image_file, plate=plate)

                now = datetime.now()
                start_date = now.replace(hour=0, minute=0, second=0)
                end_date = now.replace(hour=23, minute=59, second=59)

                park = Park.objects.filter(user=user_profile,
                                           motorcycle=motorcycle,
                                           created_at__range=(start_date, end_date),
                                           status=InOutStatus.CHECKIN,
                                           checkin__isnull=False,
                                           checkout__isnull=True).last()

                park.status = InOutStatus.CHECKOUT
                park.checkout = create_check_in_out
                park.updated_user = user_profile.user
                park.save(update_fields=['status', 'checkout', 'updated_user'])

            log.info(f'{user_profile}, {create_check_in_out}')
            return user_profile, create_check_in_out
        else:
            log.info('Unknown')
            return 'Unknown', None
