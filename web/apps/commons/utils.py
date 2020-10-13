import os
import time
from uuid import uuid4

from django.utils.deconstruct import deconstructible


@deconstructible
class RandomFileName(object):
    def __init__(self, path):
        self.path = path

    def __call__(self, _, filename):
        extension = os.path.splitext(filename)[1]
        return os.path.join(self.path, '%s-%s%s') % (time.strftime('%Y%m%d-%H%M%S'), uuid4(), extension)