from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(MEMBER)
class MEMBER(admin.ModelAdmin):
    list_display = ('first_name', 'last_name','dob','contact','email','address','MEMBERSHIP_TYPE','is_active','timestamp')
@admin.register(TRAINER)
class TRAINER(admin.ModelAdmin):
    list_display = ['first_name','last_name','SPECIALIZATION','experience','contact','email','salary','is_available','timestamp']

@admin.register(package)
class package(admin.ModelAdmin):
    list_display = ['package_name','duration','price','description','discount','start_date','end_date','is_availble','timestamp']
@admin.register(payment)
class Payment(admin.ModelAdmin):
    list_display = ['memeber_name','package_name','amount','payment_method','payment_date','receipt_no','status','is_verified','timestamp']
