from django.db import models
class Hotel(models.Model):
    name = models.CharField(max_length=100)
    owner_name = models.CharField(max_length=100)
    address= models.TextField()
    city = models.CharField(max_length=60)
    total_rooms= models.IntegerField()
    rating = models.FloatField()
    contact_number = models.CharField(max_length=20)
    is_available = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now=True)
