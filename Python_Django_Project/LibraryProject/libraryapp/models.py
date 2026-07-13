from django.db import models

class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=60)
    description = models.TextField(max_length=500)
    price = models.FloatField()
    pages_count = models.IntegerField(max_length=60)
    sold_count = models.IntegerField(max_length=60)
    is_featured = models.BooleanField(default=False)
    is_trending = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now=True)
