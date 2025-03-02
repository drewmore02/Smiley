from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CampViewSet, AreaViewSet

router = DefaultRouter()
router.register(r'camps', CampViewSet)
router.register(r'areas', AreaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]