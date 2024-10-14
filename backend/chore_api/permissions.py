from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            # Allow read access if the user is in the same household
            if hasattr(obj, 'assigned_to'):  
                return obj.assigned_to.household == request.user.profile.household
            elif hasattr(obj, 'member'):
                return obj.member.profile.household == request.user.profile.household
            return True

        if hasattr(obj, 'assigned_to'):
            return obj.assigned_to == request.user
        elif hasattr(obj, 'member'):
            return obj.member == request.user
            
        if hasattr(obj, 'assigned_to'):
            return (
                obj.assigned_to.household == request.user.profile.household and
                request.user.profile.role == 'parent'
            )
        elif hasattr(obj, 'member'):
            return obj.member == request.user

        return False