from rest_framework import permissions


class IsActiveUser(permissions.BasePermission):
    """
    Разрешение есть только у активных пользователей
    """
    def has_permission(self, request, view):
        return request.user and request.user.is_active
