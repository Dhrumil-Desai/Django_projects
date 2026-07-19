from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name','email','phone','password','profile','timestamp')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','description','image','status','timestamp')

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name','email','phone','bio','profile','total_news','status','timestamp')

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title','content','author','category','image','publish_date','publish_status','timestamp')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name','user','subject','description','timestamp']

@admin.register(Likes)
class LikesAdmin(admin.ModelAdmin):
    list_display = ('user','news','timestamp')