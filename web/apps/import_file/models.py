from django.db import models
# Create your models here.
from model_controller.models import AbstractModelController

from web.apps.commons.utils import RandomFileName


class ImportFile(AbstractModelController):
    file = models.FileField(upload_to=RandomFileName('upload/data_import'), blank=True, null=True)

    class Meta:
        verbose_name = 'Import File'
        verbose_name_plural = 'Import Files'

    def __str__(self):
        return f'[{self.created_at.date()}]: {self.file}'
