from rest_framework import serializers

from web.apps.motorcycle.serializers import MotorcycleSerializer
from web.apps.parking.models import Park


class ParkSerializer(serializers.ModelSerializer):
    motorcycle = MotorcycleSerializer(read_only=True)
    status = serializers.SerializerMethodField()

    class Meta:
        model = Park
        fields = ['motorcycle', 'created_at', 'updated_at', 'status']
        # fields = '__all__'

    def get_status(self, obj):
        '''
        Show choice
        https://docs.djangoproject.com/en/3.1/ref/models/instances/#django.db.models.Model.get_FOO_display
        '''
        return obj.get_status_display()
