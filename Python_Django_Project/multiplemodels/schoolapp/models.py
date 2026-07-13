from django.db import models
class Student(models.Model):
     name = models.CharField(max_length=100)
     phone = models.BigIntegerField()
     email = models.EmailField()
     standard = models.CharField(max_length=10)
     address = models.TextField()
     dob = models.DateField()
     age = models.IntegerField()
     gender= models.CharField(max_length=10)
     timestamp = models.DateTimeField(auto_now_add=True)

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    phone = models.BigIntegerField()
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    qualification = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    experience = models.FloatField()
    salary = models.FloatField()
    age = models.IntegerField()
    dob = models.DateField()
    timestamp = models.DateTimeField(auto_now_add=True)

class Subject(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20)
    language = models.CharField(max_length=50)
    teacher = models.CharField(max_length=60)
    totalmarks = models.FloatField()
    chapters = models.IntegerField()
    price = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

class Fees(models.Model):
    student = models.CharField(max_length=100)
    amount = models.FloatField()
    subject = models.CharField(max_length=100)
    paymentmethod = models.CharField(max_length=60)
    paymentstatus = models.CharField(max_length=60)
    timestamp = models.DateTimeField(auto_now_add=True)