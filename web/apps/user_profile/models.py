from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from model_controller.models import AbstractModelController

from web.apps.commons.utils import RandomFileName


class UserProfile(AbstractModelController):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    image = models.ImageField(upload_to=RandomFileName('upload/user_profile'), null=True, blank=True)
    family_name = models.CharField(max_length=50, db_index=True)
    last_name = models.CharField(max_length=50, blank=True, db_index=True)
    phone_number = models.CharField(max_length=15, blank=True, db_index=True)

    class Meta:
        verbose_name = 'User Profile'
        verbose_name_plural = 'User Profiles'

    def __str__(self):
        return f'{self.user}'
