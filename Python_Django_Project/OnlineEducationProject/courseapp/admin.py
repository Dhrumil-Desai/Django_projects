from django.contrib import admin
from courseapp.models import Course
# Register your models here.
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_name','trainer_name','start_date',
                    'end_date','price','duration','outcomes','languages','is_available','timestamp')