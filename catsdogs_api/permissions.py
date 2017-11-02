from rest_framework import permissions

class UpdateOwnAnimal(permissions.BasePermission):
    """allows user to edit their own cat or dog"""
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.animal_owner.id == request.user.id
