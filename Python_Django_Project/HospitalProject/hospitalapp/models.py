from django.db import models

class Patient(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=60)
    phone = models.CharField(max_length=60)
    address = models.TextField(max_length=200)
    blood_group = models.CharField(max_length=60)
    doctor_name = models.CharField(max_length=60)
    is_admitted = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now=True)