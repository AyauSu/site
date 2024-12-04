from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'description', 'publication_date']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Название книги'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Автор'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Описание'}),
            'publication_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
