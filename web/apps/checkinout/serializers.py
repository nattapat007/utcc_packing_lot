from rest_framework import serializers

from web.apps.checkinout.models import CheckIn, CheckOut
from web.apps.parking.serializers import ParkSerializer


class CheckInSerializer(serializers.ModelSerializer):
    park = ParkSerializer(many=True, read_only=True, source='park_set')

    class Meta:
        model = CheckIn
        fields = ['id', 'created_at', 'updated_at', 'face_login', 'park']


class CheckOutSerializer(serializers.ModelSerializer):
    class Meta:
        model = CheckOut
        fields = '__all__'
