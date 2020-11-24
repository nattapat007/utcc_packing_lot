from rest_framework import serializers

from web.apps.motorcycle.models import Motorcycle


class MotorcycleSerializer(serializers.ModelSerializer):
    profile = serializers.SerializerMethodField()
    phonenumber = serializers.SerializerMethodField()
    brand = serializers.SerializerMethodField()
    model = serializers.SerializerMethodField()

    class Meta:
        model = Motorcycle
        fields = ['id', 'color', 'profile', 'phonenumber', 'brand', 'model']

    def get_profile(self, obj):
        return f'{obj.profile.family_name} {obj.profile.last_name}'

    def get_phonenumber(self, obj):
        return obj.profile.phone_number

    def get_brand(self, obj):
        return obj.brand.name

    def get_model(self, obj):
        return obj.model.model_name
