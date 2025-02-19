
# apps/person/views.py
from rest_framework import generics
from .models import Person
from django.shortcuts import render
from .serializers import PersonSerializer

class PersonListView(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
