from rest_framework import permissions


class OrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.author == request.user

    def has_permission(self, request, view):
        return request.user.is_authenticated
