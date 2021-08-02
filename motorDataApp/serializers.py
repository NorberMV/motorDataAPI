from rest_framework import serializers
from .models import MotorData


class MotorDataSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = MotorData
        fields = '__all__'



