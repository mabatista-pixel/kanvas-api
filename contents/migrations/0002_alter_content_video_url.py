# Generated by Django 5.0.6 on 2024-05-20 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='video_url',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
