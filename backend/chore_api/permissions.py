from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            if hasattr(obj, 'member'):  # For Profile objects
                return obj.member.household == request.user.profile.household
            elif hasattr(obj, 'assigned_to'):  # For Task objects
                return obj.assigned_to.household == request.user.profile.household
            return True
        if hasattr(obj, 'assigned_to'):
            return (
                obj.assigned_to.household == request.user.profile.household and
                request.user.profile.role == 'parent'
            )
        elif hasattr(obj, 'member'):
            return obj.member == request.user