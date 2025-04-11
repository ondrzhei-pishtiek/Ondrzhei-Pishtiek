from django.contrib import admin
from django.urls import path
from polls import views  # Імпортуємо views з додатку polls

urlpatterns = [
    path('admin/', admin.site.urls),  # Маршрут для адмін панелі
    path('products/', views.product_list, name='product_list'),  # Маршрут для списку продуктів (якщо хочеш відображати їх на публічній сторінці)
]
