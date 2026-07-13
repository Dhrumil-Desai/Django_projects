from django.contrib import admin
from .models import Book
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ["title","category","author","price","languages","isbnNumber","edition","totalPages","publisher","publicationDate","timestamp"]