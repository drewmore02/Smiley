from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProgramViewSet, SessionViewSet

router = DefaultRouter()
router.register(r'programs', ProgramViewSet)
router.register(r'sessions', SessionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]