from django.shortcuts import get_object_or_404, render

from .models import Question


def index(request):
    all_question = Question.objects.all()
    context = {
        "all_question": all_question,
    }
    return render(request, "main/index.html", context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {
        "question": question,
    }
    return render(request, "main/detail.html", context)