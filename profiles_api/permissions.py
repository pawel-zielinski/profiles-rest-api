from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):                             # Inherits BasePermission from REST Framework's permission class.
    """Allow user to edit their own profile"""

    def has_object_permission(self, request, view, obj):                        # This method is to decide if the user has permission to do a particular action based on the following conditions:
        """Check user is trying to edit their own profile"""
        if request.method in permissions.SAFE_METHODS:                          # - user can only use safe methods on other objects,
            return True

        return obj.id == request.user.id                                        # - he can only use unsafe methods on himself.
