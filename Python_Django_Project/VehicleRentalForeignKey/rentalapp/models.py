from django.db import models

# Create your models here.
class VehicleType(models.Model):
    vehicle_type=models.CharField(max_length=100)
    fuel_type = models.CharField(max_length=100, choices=[('petrol','Petrol'),('diesel','Diesel'),('cng','CNG')])
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.vehicle_type

class Vehicle(models.Model):
    vehicle_type_id = models.ForeignKey(VehicleType,on_delete=models.CASCADE)
    vehicle_name = models.CharField(max_length=100)
    model = models.IntegerField()
    rent_per_day =models.IntegerField()
    registration_number = models.CharField(max_length=30)
    timestamp = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.vehicle_name