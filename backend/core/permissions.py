from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwnerPermission(BasePermission):
    """
    Global permission check for User Management privilege.
    """

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.has_perm(
            "custom_permissions.user_mgmt_permission"
        )

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        # check if user is owner
        return request.user == obj.created_by
