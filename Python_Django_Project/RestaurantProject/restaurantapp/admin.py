from django.contrib import admin
from .models import *

@admin.register(Restaurant)
class ShowRestaurant(admin.ModelAdmin):
    list_display = ['name','email','phone','address','total_orders',"loyalty_points",'is_active','timestamp']

@admin.register(FoodItem)
class ShowFoodItem(admin.ModelAdmin):
    list_display = ['name','category','description','price','rating','quality','is_available','timestamp']

@admin.register(Order)
class ShowOrder(admin.ModelAdmin):
    list_display = ['customer_name','food_name','quality','total_amount','payment_method','order_status','is_paid','timestamp']