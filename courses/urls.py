from django.urls import path
from .views import ListCreateCourseView, CourseDetailView, ListCreateStudentView

urlpatterns = [
    path('courses/', ListCreateCourseView.as_view()),
    path('courses/<uuid:course_id>/', CourseDetailView.as_view()),
    path('courses/<uuid:course_id>/students/', ListCreateStudentView.as_view())
]