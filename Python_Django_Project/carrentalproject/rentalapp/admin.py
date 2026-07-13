from django.contrib import admin

from .models import *


# Register your models here.
@admin.register(CUSTOMER)
class CUSTOMER(admin.ModelAdmin):
    list_display = ['name','email','contact','license_no','address','dob','is_active','timestamp']

@admin.register(CAR)
class CAR(admin.ModelAdmin):
    list_display = ['car_name','brand','model_year','registration_no','rent_per_day','fuel_type','is_available','timestamp']

@admin.register(Rental)
class Rental(admin.ModelAdmin):
    list_display = ['customer_name','carname','start_date','end_date','total_amount','status','timestamp']

@admin.register(Payment)
class Payment(admin.ModelAdmin):
    list_display = ['rental_id','amount','payment_method','status','payment_date','timestamp']