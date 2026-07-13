from django.db import models

# Create your models here.
class CUSTOMER(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    contact = models.CharField(max_length=20)
    license_no = models.CharField(max_length=100)
    address = models.TextField()
    dob = models.DateField()
    is_active = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)

class CAR(models.Model):
    car_name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    model_year = models.IntegerField()
    registration_no = models.IntegerField()
    rent_per_day = models.IntegerField()
    fuel_type= models.CharField(max_length=100, choices=[('petrol','Petrol'),('diesel','Diesel'),('electric','Electric'),('cng','Cng')])
    is_available = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)

class Rental(models.Model):
    customer_name=models.CharField(max_length=100)
    carname=models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    total_amount = models.IntegerField()
    status = models.CharField(max_length=100, choices=[('booked','Booked'),('running','Running'),('completed','Completed')])
    timestamp = models.DateTimeField(auto_now_add=True)

class Payment(models.Model):
    rental_id = models.IntegerField()
    amount = models.IntegerField()
    payment_method = models.CharField(max_length=100, choices=[('cash','Cash'),('card','Card'),('upi','Upi')])
    status= models.CharField(max_length=100, choices=[('pending','Pending'),('paid','Paid'),('failed','Failed')])
    payment_date = models.DateField()
    timestamp = models.DateTimeField(auto_now_add=True)