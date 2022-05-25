from django.http import Http404
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
    question = Question.objects.filter(pk=question_id).first()
    if question:
        response = render(
            request, "application/detail.html",
            context={
                "question": question,
            }
        )
    else:
        raise Http404("Вопрос не существует.")

    return response


def results(request, question_id):
    return HttpResponse(f"Это страница результатов по вопросу {question_id}.")


def vote(request, question_id):
    return HttpResponse(f"Вы проголосовали по вопросу {question_id}.")
