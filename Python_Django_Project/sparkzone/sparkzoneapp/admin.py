import profile
from multiprocessing.reduction import register

from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['firstName', 'lastName', 'email', 'password','profile','UserImage','timestamp']
    list_filter = ['timestamp']
    search_fields = ['firstName', 'lastName']
    list_per_page = 2
    list_display_links = ['firstName', 'lastName']

@admin.register(country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(state)
class StateAdmin(admin.ModelAdmin):
    list_display = ['country','name']

@admin.register(city)
class CityAdmin(admin.ModelAdmin):
    list_display = ['state','name']

@admin.register(userprofile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user','phone','address','country','state','city','timestamp']
    search_fields = ['state__name','timestamp']

@admin.register(category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['categoryName','description','image','categoryImage','timestamp']

@admin.register(game)
class GameAdmin(admin.ModelAdmin):
    list_display = ['category','name','description','address','city','pricePerHour','totalSystem','availableSystem','image','gameImage','timestamp']
    list_filter = ['category__categoryName']
    list_editable = ['availableSystem','image']

@admin.register(GameImages)
class GameImagesAdmin(admin.ModelAdmin):
    list_display = ['game','image','GAMEImage']

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['user','game','bookingDate','startTime','endTime','totalAmount','status','timestamp']

@admin.register(payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['user','booking','game','amount','paymentMethod','paymentStatus','paymentDate']
    list_filter = ['paymentMethod','paymentStatus']

@admin.register(reviews)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ['user','game','rating','comment','timestamp']

@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['name','email','phone','message','timestamp']