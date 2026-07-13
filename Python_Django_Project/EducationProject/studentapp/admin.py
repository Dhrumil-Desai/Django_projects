from django.contrib import admin
from .models import Student
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('full_name','email','phone','address','course','fees','attendance','is_active','timestamp')
# Register your models here.
