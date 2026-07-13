from django.db import models

# Create your models here.
class Vehicle(models.Model):
    vehicle_name=models.CharField(max_length=200)
    customer_name=models.CharField(max_length=100)
    customer_phone=models.CharField(max_length=10)
    customer_address=models.CharField(max_length=100)
    pickup_place=models.CharField(max_length=100)
    dropoff_place=models.CharField(max_length=100)
    fuel_type=models.CharField(max_length=100, choices=[("desial","Desial"),("petrol","Petrol"),("cng","CNG")])
    rental_price=models.FloatField(default=0)
    is_available=models.BooleanField(default=True)
    timestamp=models.DateTimeField(auto_now_add=True)