from rest_framework import permissions

#アクセス制限を行うファイル。
class ProfilePsermission(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return False