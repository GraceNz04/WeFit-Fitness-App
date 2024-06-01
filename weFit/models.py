from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    weight = models.FloatField()
    height = models.FloatField()
    role = models.CharField(max_length=30, default='user')
    password = models.CharField(max_length=255, default='1234')
    class Meta:
        db_table = 'users'     
           
class Workout(models.Model):
    title = models.CharField(max_length=30)
    
    def __str__(self):
        return self.title
       
class Exercise(models.Model):
    exercise_name = models.CharField(max_length=300)
    duration = models.IntegerField(help_text="Duration in seconds")
    description = models.TextField(blank=True)
    video_url = models.FileField(upload_to='static/images/gif')
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE)
    class Meta:
        db_table = 'exercise'  
    
class UserExercise(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    exercise_name = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    record = models.IntegerField(default='0')
    class Meta:
        db_table = 'user_exercise'  






