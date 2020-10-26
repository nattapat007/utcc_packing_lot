from django.contrib.auth.models import User
from django.db import models
# Create your models here.
from model_controller.models import AbstractModelController

from web.apps.user_profile.models import UserProfile


class Brand(AbstractModelController):
    name = models.CharField(max_length=100, db_index=True)

    class Meta:
        verbose_name = 'Brand'
        verbose_name_plural = 'Brands'

    def __str__(self):
        return f'{self.name}'


class Model(AbstractModelController):
    brand = models.ForeignKey(Brand, related_name='models', db_index=True, on_delete=models.CASCADE)
    model_name = models.CharField(max_length=100, db_index=True)

    class Meta:
        verbose_name = 'Model'
        verbose_name_plural = 'Models'

    def __str__(self):
        return f'{self.model_name}'


class Motorcycle(AbstractModelController):
    profile = models.OneToOneField(UserProfile, related_name='motorcycle_profile', on_delete=models.CASCADE, null=True,
                                   blank=True)
    brand = models.ForeignKey(Brand, related_name='motorcycle_brand', db_index=True, on_delete=models.SET_NULL,
                              null=True, blank=True)
    model = models.ForeignKey(Model, related_name='motorcycle_model', db_index=True, on_delete=models.SET_NULL,
                              null=True, blank=True)
    color = models.CharField(max_length=100, db_index=True)
    plate = models.CharField(max_length=100, db_index=True)

    class Meta:
        verbose_name = 'Motorcycle'
        verbose_name_plural = 'Motorcycles'

    def __str__(self):
        return f'{self.brand} {self.model} {self.plate}'
