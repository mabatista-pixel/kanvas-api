from django.db import models
import uuid


class StudentCourseStatus(models.TextChoices):
    PENDING = "pending"
    ACCEPTED = "accepted"


class StudentCourse(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    status = models.CharField(
        max_length=11,
        choices=StudentCourseStatus.choices,
        default=StudentCourseStatus.PENDING
    )
    course = models.ForeignKey("courses.Course", related_name="students_courses", on_delete=models.CASCADE)
    student = models.ForeignKey("accounts.Account", related_name="students_courses", on_delete=models.CASCADE)
