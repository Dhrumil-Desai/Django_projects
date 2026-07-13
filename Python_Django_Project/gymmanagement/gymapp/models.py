from django.db import models
class MEMBER(models.Model):
    first_name = models.CharField(max_length=100, verbose_name="First Name")
    last_name = models.CharField(max_length=100, verbose_name="Last Name")
    dob = models.DateField(verbose_name="Date of Birth")
    contact = models.CharField(max_length=10)
    email = models.EmailField()
    address = models.TextField()
    MEMBERSHIP_TYPE=models.CharField(max_length=60,choices=[('monthly','Monthly'),('quarterly','Quarterly'),
                                                            ('half-yearly','Half-Yearly'),('yearly','Yearly')])
    is_active = models.BooleanField(default=True, verbose_name="Active Status")
    timestamp = models.DateTimeField(auto_now=True)

class TRAINER(models.Model):
    first_name = models.CharField(max_length=100, verbose_name="First Name")
    last_name = models.CharField(max_length=100, verbose_name="Last Name")
    SPECIALIZATION=models.CharField(max_length=60,choices=[('cardio','Cardio'),('yoga','Yoga'),
                                                           ('weight training','Weight Training'),('crossfit','CrossFit')])
    experience = models.IntegerField()
    contact = models.CharField(max_length=10)
    email = models.EmailField()
    salary = models.IntegerField()
    is_available = models.BooleanField(default=True, verbose_name="Available Status")
    timestamp = models.DateTimeField(auto_now=True)

class package(models.Model):
    package_name = models.CharField(max_length=100)
    duration = models.IntegerField()
    price = models.IntegerField()
    description = models.TextField()
    discount = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    is_availble = models.BooleanField(default=True, verbose_name="Available Status")
    timestamp = models.DateTimeField(auto_now=True)

class payment(models.Model):
    memeber_name = models.CharField(max_length=100)
    package_name = models.CharField(max_length=100)
    amount = models.IntegerField()
    payment_method = models.CharField(max_length=100,choices=[('cash','Cash'),('upi','Upi'),
                                                              ('card','Card'),('net banking','Net Banking')])
    payment_date = models.DateField()
    receipt_no = models.IntegerField()
    status = models.CharField(choices=[('pending','Pending'),('paid','Paid'),('failed','Failed')],max_length=100)
    is_verified = models.BooleanField(default=False, verbose_name="Verified Status")
    timestamp = models.DateTimeField(auto_now=True)
