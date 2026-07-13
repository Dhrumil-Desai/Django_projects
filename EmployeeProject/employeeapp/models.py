from django.db import models
class Employee(models.Model):
    full_name = models.CharField(max_length=100)
    email=models.EmailField(max_length=50)
    phone = models.CharField(max_length=20)
    department = models.CharField(max_length=200)
    designation = models.CharField(max_length=50)
    salary=models.FloatField(max_length=50)
    joining_date=models.DateField()
    is_active = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now=True)
