from typing import Any
from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework.request import Request
from rest_framework.views import APIView

class IsAdminOrReadOnly(BasePermission):
    """
    Custom permission that allows any authenticated user to perform read-only
    requests (GET, HEAD, OPTIONS), but only allows users with role 'admin'
    to perform write operations (POST, PUT, PATCH, DELETE).
    """
    def has_permission(self, request: Request, view: APIView) -> bool:
        if request.method in SAFE_METHODS:
            return bool(request.user and request.user.is_authenticated)
        
        # For non-safe methods, only allow if the user's role is 'admin'
        return bool(request.user and getattr(request.user, 'role', None) == 'admin')

