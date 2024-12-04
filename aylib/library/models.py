from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)  # Название книги
    author = models.CharField(max_length=100)  # Автор книги
    description = models.TextField()  # Описание
    publication_date = models.DateField()  # Дата публикации
    created_at = models.DateTimeField(auto_now_add=True)  # Дата добавления

    def __str__(self):
        return self.title
