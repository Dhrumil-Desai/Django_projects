from django.contrib import admin
from .models import *

@admin.register(Customer)
class ShowFoodItem(admin.ModelAdmin):
    list_display = ['name','email','phone','city','address','is_active','timestamp']

@admin.register(Stylist)
class ShowRestaurant(admin.ModelAdmin):
    list_display = ['name','specialization','phone','salary','experience',"is_active",'timestamp']

@admin.register(Service)
class ShowOrder(admin.ModelAdmin):
    list_display = ['service_name','duration','price','category','description','is_active','timestamp']