import os
import time
from uuid import uuid4

from django.utils.deconstruct import deconstructible
from model_controller.utils import EXCLUDE_MODEL_CONTROLLER_FIELDS

EXCLUDE_COMMON_FIELDS = EXCLUDE_MODEL_CONTROLLER_FIELDS + ('alive',)


@deconstructible
class RandomFileName(object):
    def __init__(self, path):
        self.path = path

    def __call__(self, _, filename):
        extension = os.path.splitext(filename)[1]
        return os.path.join(self.path, '%s-%s%s') % (time.strftime('%Y%m%d-%H%M%S'), uuid4(), extension)
