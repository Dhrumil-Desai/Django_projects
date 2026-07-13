from django.contrib import admin
from .models import Employee
@admin.register(Employee)
class Employee(admin.ModelAdmin):
    list_display = ('full_name','email','phone','department','designation','salary','joining_date','is_active','timestamp')
# Register your models here.