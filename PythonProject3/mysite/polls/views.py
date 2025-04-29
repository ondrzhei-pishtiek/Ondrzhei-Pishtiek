from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import Question


# Функція для відображення списку питань
def question_list(request):
    questions = Question.objects.all()  # отримуємо всі питання
    return render(request, 'polls/question_list.html', {'questions': questions})


# Функція для реєстрації
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # зберігаємо користувача
            messages.success(request, 'Ваш акаунт створено!')
            return redirect('login')  # перенаправляємо на сторінку входу після реєстрації
        else:
            messages.error(request, 'Щось пішло не так. Перевірте форму.')
    else:
        form = UserCreationForm()  # якщо GET-запит, виводимо порожню форму

    return render(request, 'registration/register.html', {'form': form})
