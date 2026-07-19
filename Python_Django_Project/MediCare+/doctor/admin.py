from django.contrib import admin
from .models import *
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('fName','lName','email','password','profile_pic','userprofileimage','date_joined')
    list_display_links = ('fName','lName')
    search_fields = ('fName', 'lName')
    list_filter = ['date_joined']
    list_per_page = 1

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ['country','name']

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ['state','name']

@admin.register(DoctorSpecialization)
class DoctorSpecializationAdmin(admin.ModelAdmin):
    list_display = ['name','description','image','specializationImage']

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ['country','state','city','user','specialization','experience_years','qualification',
                    'consultation_fees','phone','address','available_from',
                    'available_to','bio','image','doctorImage','created_at']
    list_display_links = ['user']
    list_editable = ('experience_years','consultation_fees',)
    search_fields = ('user__fName','qualification',)
    list_filter = ('specialization','country','state',)
    list_per_page = 1

@admin.register(PatientProfile)
class PatientProfileAdmin(admin.ModelAdmin):
    list_display = ['user','dob','gender','blood_group','address','phone_no','image','patientImage']
    list_display_links = ['user']
    list_editable = ('address','phone_no')
    search_fields = ('user__fName','phone_no')
    list_filter = ('gender','blood_group',)
    list_per_page = 1

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['patient','doctor','appointment_date','time_slot','symptoms','status','created_at']
    list_display_links = ['patient']
    list_editable = ['status']
    search_fields = ('patient__fName','doctor__user__fName',)
    list_filter = ('status','appointment_date')
    list_per_page = 1

@admin.register(Prescription)
class PrescriptionAdmin(admin.ModelAdmin):
    list_display = ['appointment','doctor_notes','medicines','next_visit_date','created_at']

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['user','appointment','amount','payment_method','status','payment_date']
    list_display_links = ['user']
    list_editable = ['status']
    search_fields = ('user__fName',)
    list_filter = ('payment_method','status',)
    list_per_page = 1


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['user','doctor','rating','comment','created_at']
    list_display_links = ['user']
    list_editable = ['rating']
    search_fields = ('user__fName','doctor__user__fName',)
    list_filter = ['rating']
    list_per_page = 1


@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['name','email','phone','message','created_at']