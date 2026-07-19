from django.contrib import admin
from .models import *
@admin.register(country)
class country(admin.ModelAdmin):
    list_display = ('country_name', 'country_code','timestamp')

@admin.register(state)
class state(admin.ModelAdmin):
    list_display = ('country_id','state_name','state_code','timestamp')

@admin.register(city)
class city(admin.ModelAdmin):
    list_display = ('country_id','state_id','city_name','pincode','timestamp')

@admin.register(agent)
class agent(admin.ModelAdmin):
    list_display = ['country_id','state_id','city_id','agent_name','email','phone',
                    'profile_image','agentimage','experience','timestamp']

@admin.register(PROPERTYCATEGORY)
class PROPERTYCATEGORY(admin.ModelAdmin):
    list_display = ['category_name','category_image','propertyimage','description','timestamp']

@admin.register(PROPERTY)
class PROPERTY(admin.ModelAdmin):
    list_display = ['category_id','agent_id','property_title','description','property_type',
                    'price','address','property_image','property','timestamp']

@admin.register(customers)
class customers(admin.ModelAdmin):
    list_display = ['country_id','state_id','city_id','customer_name','email','phone',
                    'profile_image','customerimage','timestamp']

@admin.register(propertyvisit)
class propertyvisit(admin.ModelAdmin):
    list_display = ['customer_id','property_id','visit_date','visit_time','status','timestamp']

@admin.register(propertyinquiry)
class propertyinquiry(admin.ModelAdmin):
    list_display = ['customer_id','property_id','message','status','timestamp']

@admin.register(propertybooking)
class propertybooking(admin.ModelAdmin):
    list_display = ['customer_id','property_id','booking_amount','booking_date','status','timestamp']

@admin.register(payment)
class Payment(admin.ModelAdmin):
    list_display = ['booking_id','amount','payment_method','transaction_id','payment_status','timestamp']

@admin.register(review)
class review(admin.ModelAdmin):
    list_display = ['customer_id','property_id','rating','comment','timestamp']