from django.urls import path
from .views import CreateCourseContentView, CourseContentDetailView


urlpatterns = [
    path('courses/<uuid:course_id>/contents/', CreateCourseContentView.as_view()),
    path('courses/<uuid:course_id>/contents/<uuid:content_id>/', CourseContentDetailView.as_view())
]
