from django.db import models


class InOutStatus(models.IntegerChoices):
    CHECKIN = 0, 'Check-in'
    CHECKOUT = 1, 'Check-out'
