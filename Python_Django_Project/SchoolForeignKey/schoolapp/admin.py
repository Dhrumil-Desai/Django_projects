from django.contrib import admin
from .models import *
@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['teacher_name','subject','qualification','contact','timestamp']
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['teacher_id','student_name','standard','roll_number','contact','timestamp']