from django.db import models
class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=60)
    price = models.FloatField()
    quality=models.IntegerField()
    brand = models.CharField()
    is_active = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)

class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    city = models.CharField(max_length=60)
    address = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)

class Order(models.Model):
    customer_name = models.CharField(max_length=100)
    product_name = models.CharField(max_length=100)
    quality = models.IntegerField()
    total_price = models.FloatField()
    payment_status = models.CharField(max_length=100)
    is_active = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

