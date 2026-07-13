from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()
    category = models.CharField(max_length=100, choices=[("clothes","Clothes"),("electronics","Electronics"),("","")])
    #above code right side shows in front end and left side shows in left side
    brand = models.CharField(max_length=100)
    qty = models.IntegerField()
    image = models.URLField(null=True, blank=True)
    status = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now=True)

class Supplier(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    email = models.EmailField()
    website = models.URLField(null=True, blank=True)
    address = models.TextField()
    timestamp = models.DateTimeField(auto_now=True)

class Warehouse(models.Model):
    name = models.CharField(max_length=100)
    phone= models.BigIntegerField()
    email = models.EmailField()
    address = models.TextField()
    workercount = models.IntegerField()
    capacity = models.CharField(max_length=60, choices=[("small","Small"),("medium","Medium"),("large","Large"), ("extralarge","Extralarge")])
    manager= models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now=True)

class Customer(models.Model):
    name = models.CharField(max_length=100)
    phone = models.BigIntegerField()
    email = models.EmailField()
    gender = models.CharField(max_length=60, choices=[("male","Male"),("female","Female"),("other","Other")])
    address = models.TextField()
    status = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now=True)

class Order(models.Model):
    customer= models.CharField(max_length=100)
    product = models.CharField(max_length=100)
    qty = models.IntegerField()
    amount = models.FloatField()
    order_status = models.CharField(max_length=60, choices=[("confirmed","Confirmed"),("pending","Pending"),("cancelled","Cancelled")])
    timestamp = models.DateTimeField(auto_now=True)

class Payment(models.Model):
    order = models.CharField(max_length=100)
    paymentmethod = models.CharField(max_length=100, choices=[("cash","Cash"),("upi","Upi"),("credit card","Credit Card"),("net banking","Net Banking")])
    payment_status = models.CharField(max_length=60, choices=[("paid", "Paid"), ("processing", "Processing"),("failed", "Failed")])
    totalamount = models.FloatField()
    timestamp = models.DateTimeField(auto_now=True)