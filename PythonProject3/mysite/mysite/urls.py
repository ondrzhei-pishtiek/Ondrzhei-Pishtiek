from django.contrib import admin
from django.urls import path, include
from polls.views import question_list, register_view  # імпортуємо функції
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', question_list, name='question_list'),  # маршрут для списку питань
    path('register/', register_view, name='register'),  # маршрут для реєстрації
    path('polls/', include('polls.urls')),  # підключення додаткових маршрутів з app "polls"
    path('login/', auth_views.LoginView.as_view(), name='login'),
]
