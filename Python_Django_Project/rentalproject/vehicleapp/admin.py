from django.contrib import admin

from vehicleapp.models import Vehicle


# Register your models here.
@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ["vehicle_name",'customer_name','customer_phone',
                    'customer_address','pickup_place','dropoff_place',
                    'fuel_type','rental_price','is_available','timestamp']