from rest_framework import serializers
from web.apps.parking.serializers import ParkSerializer
from web.apps.checkinout.models import CheckIn, CheckOut


class CheckInSerializer(serializers.ModelSerializer):
    park = ParkSerializer(many=True, read_only=True, source='park_set')

    class Meta:
        model = CheckIn
        fields = ['id', 'created_at', 'updated_at', 'face_login', 'park', 'plate']


class CheckOutSerializer(serializers.ModelSerializer):
    park = ParkSerializer(many=True, read_only=True, source='park_set')

    class Meta:
        model = CheckOut
        fields = ['id', 'created_at', 'updated_at', 'face_logout', 'park', 'plate']
