from django.contrib import admin
from .models import *
@admin.register(team)
class team(admin.ModelAdmin):
    list_display = ['team_name','coach_name','captain_name','timestamp']

@admin.register(Player)
class player(admin.ModelAdmin):
    list_display = ['team_id','player_name','role','age','country','timestamp']