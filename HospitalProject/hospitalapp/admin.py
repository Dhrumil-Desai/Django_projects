from django.contrib import admin
from .models import Patient
@admin.register(Patient)
class Patient(admin.ModelAdmin):
    list_display = ['name','age','gender','phone','address','blood_group','doctor_name','is_admitted','timestamp']
# Register your models here.
