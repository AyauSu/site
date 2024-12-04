from django.contrib import admin
from .models import Book

# Регистрируем модель Book в админке
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_date', 'created_at')
    search_fields = ('title', 'author')
    list_filter = ('publication_date',)
    ordering = ('-created_at',)
