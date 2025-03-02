from rest_framework import viewsets
from .models import Camp, Area
from .serializers import CampSerializer, AreaSerializer
from apps.users.permissions import IsAdminOrReadOnly

class CampViewSet(viewsets.ModelViewSet):
    queryset = Camp.objects.all()
    serializer_class = CampSerializer
    permission_classes = [IsAdminOrReadOnly]

class AreaViewSet(viewsets.ModelViewSet):
    queryset = Area.objects.all()
    serializer_class = AreaSerializer
    permission_classes = [IsAdminOrReadOnly]