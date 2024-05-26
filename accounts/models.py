from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
from students_courses.models import StudentCourse


class Account(AbstractUser):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    email = models.CharField(max_length=100, unique=True)
    my_courses = models.ManyToManyField("courses.Course", through=StudentCourse)





