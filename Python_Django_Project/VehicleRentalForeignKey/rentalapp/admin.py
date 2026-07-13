from django.contrib import admin
from .models import *
@admin.register(VehicleType)
class VehicleType(admin.ModelAdmin):
    list_display = ['vehicle_type','fuel_type','description','timestamp']

@admin.register(Vehicle)
class Vehicle(admin.ModelAdmin):
    list_display = ['vehicle_type_id','vehicle_name','model','rent_per_day','registration_number','timestamp']