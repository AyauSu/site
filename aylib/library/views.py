from django.contrib.auth import login
from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from django.contrib.auth.forms import UserCreationForm
from .forms import BookForm
from django.contrib.auth import logout

# Список книг
def index(request):
    books = Book.objects.all()
    return render(request, 'library/index.html', {'books': books})

# Контакты
def contacts(request):
    return render(request, 'library/contacts.html')

# Создание новой книги
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = BookForm()
    return render(request, 'library/add_book.html', {'form': form})

def view_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'library/view_book.html', {'book': book})

# Редактирование книги
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = BookForm(instance=book)
    return render(request, 'library/edit_book.html', {'form': form, 'book': book})
# Удаление книги
def delete_book(request, book_id):
        book = get_object_or_404(Book, id=book_id)
        if request.method == "POST":
            book.delete()
            return redirect('index')
        return render(request, 'library/delete_book.html', {'book': book})


# Registration
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Автоматический вход после регистрации
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'library/register.html', {'form': form})

def custom_logout(request):
    logout(request)
    return redirect('index')

