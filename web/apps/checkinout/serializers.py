from rest_framework import serializers
from web.apps.parking.serializers import ParkSerializer
from web.apps.checkinout.models import CheckIn, CheckOut

from drf_extra_fields.fields import Base64ImageField


class CheckInSerializer(serializers.ModelSerializer):
    face_login = Base64ImageField()
    park = ParkSerializer(many=True, read_only=True, source='park_set')

    class Meta:
        model = CheckIn
        fields = ['id', 'created_at', 'updated_at', 'face_login', 'park', 'plate']


class CheckOutSerializer(serializers.ModelSerializer):
    face_logout = Base64ImageField()
    park = ParkSerializer(many=True, read_only=True, source='park_set')

    class Meta:
        model = CheckOut
        fields = ['id', 'created_at', 'updated_at', 'face_logout', 'park', 'plate']
