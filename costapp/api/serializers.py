from dataclasses import fields
from rest_framework import serializers

from costapp.models import MyCost


class MyCostSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyCost
        fields = '__all__'
