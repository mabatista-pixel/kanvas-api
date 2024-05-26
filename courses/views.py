from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveUpdateAPIView
from .models import Course
from .serializers import CourseSerializer
from .permissions import MyCustomPermission
from courses.serializers import StudentTest
from rest_framework.response import Response
from rest_framework import status
from accounts.models import Account


class ListCreateCourseView(ListCreateAPIView):
    permission_classes = [MyCustomPermission]

    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Course.objects.all()
        else:
            return Course.objects.filter(students=self.request.user)
            

class CourseDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = [MyCustomPermission]
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    lookup_url_kwarg = "course_id"


class ListCreateStudentView(RetrieveUpdateAPIView):

    serializer_class = StudentTest
    lookup_url_kwarg = "course_id"
    queryset = Course.objects.all()

    def update(self, request, *args, **kwargs):
        course = self.get_object()

        for item in request.data.get("students_courses"):
            student_email = item["student_email"]
       
            if not student_email:
                return Response(
                    {"detail": f"No active accounts was found: {student_email}."}, 
                    status=status.HTTP_400_BAD_REQUEST
                )
            try:
                student = Account.objects.get(email=student_email)
            except Account.DoesNotExist:
                return Response(
                    {"detail": f"No active accounts was found: {student_email}."},
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            course.students.add(student)
            course.save()
            serializer = self.get_serializer(course)
            return Response(serializer.data)

 




