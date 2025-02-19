# apps/person/serializers.py

from rest_framework import serializers
from .models import Person

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        # You can list the fields explicitly or use '__all__' to include every field.
        fields = '__all__'