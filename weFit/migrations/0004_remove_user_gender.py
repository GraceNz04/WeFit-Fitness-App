# Generated by Django 4.2.13 on 2024-06-01 11:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weFit', '0003_alter_exercise_video_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='gender',
        ),
    ]