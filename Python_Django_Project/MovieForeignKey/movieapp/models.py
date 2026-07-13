from django.db import models
class MovieCategory(models.Model):
    categoryname = models.CharField(max_length=100)
    categorydescription = models.TextField()
    timestamp = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.categoryname

class Director(models.Model):
    directorname = models.CharField(max_length=100)
    directorbio =models.TextField()
    timestamp = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.directorname

class Movie(models.Model):
    movietitle = models.CharField(max_length=100)
    categoryid = models.ForeignKey(MovieCategory, on_delete=models.CASCADE)
    directorid = models.ForeignKey(Director, on_delete=models.CASCADE)
    duration =models.IntegerField()
    releasedate = models.DateTimeField()
    language = models.CharField(max_length=100)
    rating =models.FloatField()
    timestamp = models.DateTimeField(auto_now=True)