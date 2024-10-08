from rest_framework.permissions import BasePermission



class IsOwnerOrReadOnly(BasePermission):
    """
    Permission to allow users edit or delete their Reviews
    """

    def has_object_permission(self, request, view, obj):
        return obj == request.user