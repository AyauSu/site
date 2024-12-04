from django.contrib import admin
from django.urls import path, include  # Импорт include для подключения маршрутов приложения

urlpatterns = [
    path('admin/', admin.site.urls),  # Маршрут для панели администратора
    path('', include('library.urls')),  # Подключение маршрутов приложения library
]
