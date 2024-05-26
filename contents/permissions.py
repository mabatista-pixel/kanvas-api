from rest_framework import permissions


class CreateContentPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_superuser and request.user.is_authenticated:
            return True
        

class IsSuperUserOrParticipant(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        return request.method in permissions.SAFE_METHODS

    def has_object_permission(self, request, view, obj):
        return request.user in obj.course.students.all() or request.user.is_superuser
