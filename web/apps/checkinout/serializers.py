from rest_framework import serializers

from web.apps.checkinout.models import CheckIn, CheckOut


class CheckInSerializer(serializers.ModelSerializer):
    class Meta:
        model = CheckIn
        fields = '__all__'


class CheckOutSerializer(serializers.ModelSerializer):
    class Meta:
        model = CheckOut
        fields = '__all__'
