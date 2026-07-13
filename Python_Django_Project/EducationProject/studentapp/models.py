from django.db import models

class Student(models.Model):
    full_name = models.CharField(max_length=100)
    email=models.EmailField(max_length=50)
    phone = models.CharField(max_length=20)
    address = models.TextField(max_length=200)
    course = models.CharField(max_length=50)
    fees=models.FloatField(max_length=50)
    attendance=models.IntegerField(default=0)
    is_active = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now=True)