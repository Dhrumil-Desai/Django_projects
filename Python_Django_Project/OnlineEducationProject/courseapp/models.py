from django.db import models

# Create your models here.
class Course(models.Model):
    course_name = models.CharField(max_length=100)
    trainer_name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    price= models.IntegerField()
    duration = models.IntegerField()
    outcomes= models.TextField()
    languages = models.CharField(max_length=100, choices=[("english","English"),("hindi","Hindi")])
    is_available=models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)
