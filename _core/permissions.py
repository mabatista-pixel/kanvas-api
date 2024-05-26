from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsSuperUser(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_superuser


class IsAuthenticated(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated


class IsCourseParticipantOrSuperUser(BasePermission):
    def has_permission(self, request, view):
        course_id = view.kwargs.get('course_id')
        if request.user.is_superuser:
            return True
        return CourseStudent.objects.filter(course_id=course_id, student=request.user).exists()