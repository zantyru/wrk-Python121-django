from django.shortcuts import render, HttpResponse
from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # output = ', '.join(f"&laquo;{q.question_text}&raquo;" for q in latest_question_list)

    return render(
        request,
        "application/index.html",
        context={'latest_question_list': latest_question_list}
    )


def detail(request, question_id):
    return HttpResponse(f"Это вопрос {question_id}.")


def results(request, question_id):
    return HttpResponse(f"Это страница результатов по вопросу {question_id}.")


def vote(request, question_id):
    return HttpResponse(f"Вы проголосовали по вопросу {question_id}.")
