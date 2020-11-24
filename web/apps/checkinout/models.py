from django.db import models
# Create your models here.
from model_controller.models import AbstractTimeStampMarker

from web.apps.commons.utils import RandomFileName
from web.apps.motorcycle.models import Motorcycle

check_in_out_upload_to = 'upload/check_in_out/'


class CheckIn(AbstractTimeStampMarker):
    face_login = models.ImageField(upload_to=RandomFileName(f'{check_in_out_upload_to}face_login'),
                                   null=True,
                                   blank=True)
    plate = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f'{self.face_login}'


class CheckOut(AbstractTimeStampMarker):
    face_logout = models.ImageField(upload_to=RandomFileName(f'{check_in_out_upload_to}face_logout'),
                                    null=True,
                                    blank=True)
    plate = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f'{self.face_logout}'
