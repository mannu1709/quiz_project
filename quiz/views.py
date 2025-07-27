from django.shortcuts import render, redirect
from .models import Quiz, Question
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache


# Create your views here.
@never_cache
@login_required(login_url='/accounts/login/')
def home(request):
    quizzes = Quiz.objects.all()
    return render(request, 'quiz/home.html', {'quizzes': quizzes})


def quiz_detail(request, quiz_id):
    quiz = Quiz.objects.get(pk=quiz_id)
    questions = quiz.question_set.all()

    if request.method == 'POST':
        score = 0
        for q in questions:
            selected = request.POST.get(str(q.id))
            if selected == q.correct_option:
                score += 1
        return render(request, 'quiz/result.html', {'score': score, 'total': questions.count()})

    return render(request, 'quiz/quiz_detail.html', {'quiz': quiz, 'questions': questions})

