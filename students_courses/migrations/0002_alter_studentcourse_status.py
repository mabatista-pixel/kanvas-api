# Generated by Django 5.0.6 on 2024-05-20 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students_courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentcourse',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('accepted', 'Accepted')], default='pending', max_length=11),
        ),
    ]
