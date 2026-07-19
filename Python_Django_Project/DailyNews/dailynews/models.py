from os import name

from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.BinaryField()
    password = models.CharField(max_length=100)
    profile = models.URLField( null=True, blank=True)
    timestamp = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.URLField(null=True, blank=True)
    status = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField()
    phone = models.BigIntegerField()
    bio = models.TextField()
    profile= models.URLField(null=True, blank=True)
    total_news = models.IntegerField()
    status = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class News(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.URLField(null=True, blank=True)
    publish_date = models.DateField()
    publish_status = models.CharField(max_length=60, choices=[('published','Published'),('draft','Draft')])
    timestamp = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    name = models.ForeignKey(News, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Likes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=True)
