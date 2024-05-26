from rest_framework import serializers
from .models import Course
from students_courses.serializers import StudentCourseSerializer


class CourseSerializer(serializers.ModelSerializer):
        
    class Meta: 
        model = Course
        fields = ["id", "name", "status", "start_date", "end_date", "instructor", "students_courses", "contents"]
        read_only_fields = "students_courses", "contents"


class StudentTest(serializers.ModelSerializer):
    students_courses = StudentCourseSerializer(many=True)

    class Meta:
        model = Course
        fields = ["id", "name", "students_courses"]
        depth = 1
        extra_kwargs = {"name": {"read_only": True}}

 