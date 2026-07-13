from django.contrib import admin
from .models import Hotel
@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ('name','owner_name','address','city','total_rooms', 'rating', 'contact_number', 'is_available','timestamp')