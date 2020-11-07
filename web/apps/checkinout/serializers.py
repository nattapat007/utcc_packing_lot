from rest_framework import serializers

from web.apps.parking.models import Park


class CheckInSerializer(serializers.ModelSerializer):
    class Meta:
        model = Park
        fields = '__all__'
