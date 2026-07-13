from django.db import models
class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    city = models.CharField(max_length=60)
    address = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)

class Stylist(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    salary = models.FloatField()
    experience = models.IntegerField()
    is_active = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)

class Service(models.Model):
    service_name = models.CharField(max_length=100)
    duration = models.IntegerField()
    price = models.FloatField()
    category = models.CharField(max_length=20)
    description = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)
