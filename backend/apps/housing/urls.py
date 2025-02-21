from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HousingAreaViewSet, CabinViewSet, RoomViewSet

router = DefaultRouter()
router.register(r'areas', HousingAreaViewSet)
router.register(r'cabins', CabinViewSet)
router.register(r'rooms', RoomViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
