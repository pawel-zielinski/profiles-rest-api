from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):                             # Inherits BasePermission from REST Framework's permission class.
    """Allow user to edit their own profile"""

    def has_object_permission(self, request, view, obj):                        # This method is to decide if the user has permission to do a particular action based on the following conditions:
        """Check user is trying to edit their own profile"""
        if request.method in permissions.SAFE_METHODS:                          # - user can only use safe methods on other objects,
            return True

        return obj.id == request.user.id                                        # - he can only use unsafe methods on himself.


class UpdateOwnStatus(permissions.BasePermission):                              # Very similar to the UpdateOwnProfile class but it is for updating the users own status.
    """Allow users to update their own status"""

    def has_object_permission(self, request, view, obj):
        """Check the user is trying to update their own status"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user_profile.id == request.user.id
