from django.contrib import admin
from .models import *
@admin.register(Student)
# Register your models here.
class ShowStudents(admin.ModelAdmin):
    list_display = ('name','phone','email','standard','address','dob','age','gender','timestamp')

@admin.register(Teacher)
class ShowTeachers(admin.ModelAdmin):
    list_display = ('name','phone','email','subject','qualification','experience','gender','salary','age','dob','timestamp')

@admin.register(Subject)
class ShowSubjects(admin.ModelAdmin):
    list_display = ('name','code','language','teacher','totalmarks','chapters','price','timestamp')

@admin.register(Fees)
class ShowFees(admin.ModelAdmin):
    list_display = ['student','amount','subject','paymentmethod','paymentstatus','timestamp']