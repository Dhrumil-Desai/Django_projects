from django.contrib import admin
from .models import *

@admin.register(Product)
class ShowRestaurant(admin.ModelAdmin):
    list_display = ['name','category','price','quality','brand',"is_active",'timestamp']

@admin.register(Customer)
class ShowFoodItem(admin.ModelAdmin):
    list_display = ['name','email','phone','city','address','is_active','timestamp']

@admin.register(Order)
class ShowOrder(admin.ModelAdmin):
    list_display = ['customer_name','product_name','quality','total_price','payment_status','is_active','timestamp']