from django.contrib import admin
from .models import *
@admin.register(MovieCategory)
class MovieMovieCategory(admin.ModelAdmin):
    list_display = ['categoryname','categorydescription','timestamp']

@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ['directorname','directorbio','timestamp']

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['movietitle','categoryid','directorid','duration','releasedate','language','rating','timestamp']
