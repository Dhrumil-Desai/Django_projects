from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    author = models.CharField(max_length=60)
    price = models.FloatField()
    languages = models.CharField(max_length=100)
    isbnNumber = models.BigIntegerField()
    edition = models.CharField(max_length=10)
    totalPages = models.IntegerField()
    publisher = models.CharField(max_length=60)
    publicationDate = models.DateField()
    timestamp = models.DateTimeField(auto_now=True)