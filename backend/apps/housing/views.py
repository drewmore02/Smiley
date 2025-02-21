from rest_framework import viewsets
from .models import HousingArea, Cabin, Room
from .serializers import HousingAreaSerializer, CabinSerializer, RoomSerializer
from .permissions import IsAdminOrReadOnly

class HousingAreaViewSet(viewsets.ModelViewSet):
    queryset = HousingArea.objects.all()
    serializer_class = HousingAreaSerializer
    permission_classes = [IsAdminOrReadOnly]

class CabinViewSet(viewsets.ModelViewSet):
    queryset = Cabin.objects.all()
    serializer_class = CabinSerializer
    permission_classes = [IsAdminOrReadOnly]

class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [IsAdminOrReadOnly]

