from rest_framework import serializers
from .models import HousingArea, Cabin, Room

class HousingAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = HousingArea
        fields = '__all__'

class CabinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cabin
        fields = '__all__'

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'