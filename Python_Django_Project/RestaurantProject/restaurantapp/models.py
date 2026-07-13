from django.db import models
class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    address = models.TextField(max_length=100)
    total_orders=models.IntegerField()
    loyalty_points = models.IntegerField()
    is_active = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)

class FoodItem(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()
    rating = models.FloatField()
    quality = models.IntegerField()
    is_available = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)

class Order(models.Model):
    customer_name = models.CharField(max_length=100)
    food_name = models.CharField(max_length=100)
    quality = models.IntegerField()
    total_amount = models.FloatField()
    payment_method = models.CharField(max_length=100)
    order_status = models.CharField(max_length=100)
    is_paid = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

