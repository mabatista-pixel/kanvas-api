from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import ContentSerializer
from courses.models import Course
from .models import Content
from .permissions import CreateContentPermission, IsSuperUserOrParticipant
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import NotFound
from rest_framework_simplejwt.authentication import JWTAuthentication


class CreateCourseContentView(CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [CreateContentPermission]

    serializer_class = ContentSerializer
    queryset = Content.objects.all()
    lookup_url_kwarg = "course_id"

    def perform_create(self, serializer):
        found_course = Course.objects.get(id=self.kwargs["course_id"])
        if not found_course:
            raise NotFound({"detail": "course not found."})
        serializer.save(course=found_course)
    

class CourseContentDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsSuperUserOrParticipant]
    serializer_class = ContentSerializer
    queryset = Content.objects.all()
    lookup_url_kwarg = "course_id"

    def get_object(self):
        try:
            Course.objects.get(id=self.kwargs["course_id"])
            content = Content.objects.get(id=self.kwargs["content_id"]) 
        except Content.DoesNotExist:
            raise NotFound({"detail": "content not found."})
        except Course.DoesNotExist:
            raise NotFound({"detail": "course not found."})
        self.check_object_permissions(self.request, content)
        return content

   
