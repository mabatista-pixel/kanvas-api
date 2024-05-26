from django.db import models
import uuid
from students_courses.models import StudentCourse


class CourseStatus(models.TextChoices):
    NOT_STARTED = "not started"
    IN_PROGRESS = "in progress"
    FINISHED = "finished"


class Course(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=100, unique=True, null=False)
    status = models.CharField(
        max_length=11,
        choices=CourseStatus.choices,
        default=CourseStatus.NOT_STARTED
    )
    start_date = models.DateField(null=False)
    end_date = models.DateField(null=False)
    instructor = models.ForeignKey("accounts.Account", on_delete=models.CASCADE, related_name="courses", null=True)
    students = models.ManyToManyField("accounts.Account", through=StudentCourse, related_name="estudante")