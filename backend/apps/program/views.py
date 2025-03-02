from rest_framework import viewsets
from .models import Program, Session
from .serializers import ProgramSerializer, SessionSerializer
from apps.users.permissions import IsAdminOrReadOnly

class ProgramViewSet(viewsets.ModelViewSet):
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer
    permission_classes = [IsAdminOrReadOnly]

class SessionViewSet(viewsets.ModelViewSet):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer
    permission_classes = [IsAdminOrReadOnly]
