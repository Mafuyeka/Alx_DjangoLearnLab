from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_filter = ('publication_year',)
    search_fields = ('title', 'author')
