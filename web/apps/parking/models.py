from django.db import models

# Create your models here.
from model_controller.models import AbstractModelController

from web.apps.motorcycle.models import Motorcycle
from web.apps.user_profile.models import UserProfile


class Park(AbstractModelController):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, db_index=True)
    motorcycle = models.ForeignKey(Motorcycle, on_delete=models.CASCADE, db_index=True)

    class Meta:
        verbose_name = 'Park'
        verbose_name_plural = 'Parks'

    def __str__(self):
        return f'{self.motorcycle}, {self.user}'
