from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from .models import Question

def question_list(request):
    questions = Question.objects.all()
    return render(request, 'polls/question_list.html', {'questions': questions})
