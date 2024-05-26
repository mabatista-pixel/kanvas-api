# Generated by Django 5.0.6 on 2024-05-21 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_account_my_courses'),
        ('courses', '0003_alter_course_instructor'),
        ('students_courses', '0002_alter_studentcourse_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='my_courses',
            field=models.ManyToManyField(through='students_courses.StudentCourse', to='courses.course'),
        ),
    ]
