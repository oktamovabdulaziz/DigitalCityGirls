from django.shortcuts import redirect, render
from django.utils.dateparse import parse_duration
from main.models import *
from adminstrator.forms import QuestionForm
from django.shortcuts import get_object_or_404


def index_view(request):
    form = QuestionForm
    context = {
        "digital": Digital.objects.all(),
        "forms": form

    }
    return render(request, 'dashboard.html', context)


def direction_view(request):
    context = {
        "direction": Direction.objects.all(),
    }
    return render(request, 'direction.html', context)


def create_direction_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        photo = request.FILES.get("photo")
        time = parse_duration(request.POST.get("time"))
        is_logic = request.POST.get("is_logic")
        question_count = request.POST.get("question_count")
        Direction.objects.create(
            name=name,
            photo=photo,
            time=time,
            is_logic=True if is_logic == "on" else False,
            question_count=question_count,
        )
    return redirect("direction")


def user_view(request):
    context = {
        "user": User.objects.all(),
    }
    return render(request, "user.html", context)


def digital_view(request):
    context = {
        "digital": Digital.objects.all(),
    }
    return render(request, "digital.html", context)


def create_digital_view(request):
    if request.method == 'POST':
        logo = request.FILES.get("logo")
        bg_image = request.FILES.get("bg_image")
        name = request.POST["name"]
        digital = Digital.objects.create(
            logo=logo,
            bg_image=bg_image,
            name=name,
        )
        digital.save()
    return redirect("digital")


def question_view(request):
    form = QuestionForm
    context = {
        "question": Question.objects.all(),
        "form": form,
    }
    return render(request, "question.html", context)


def question_list_view(request):
    context = {
        'question': Question.objects.all()
    }
    return render(request, 'question-list.html', context)


def create_question(request):
    directions = Direction.objects.all()

    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()

        return redirect('question-list')
    return render(request, 'question.html', {'directions': directions})


def question_edit(request, pk):
    obj = get_object_or_404(Question, id=pk)

    if request.method == 'GET':
        context = {'form': QuestionForm(instance=obj), 'id': pk}
        return render(request, 'question.html', context)

    elif request.method == 'POST':
        form = QuestionForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('create-question')
        else:
            context = {'form': form, 'id': pk}
            return render(request, 'question.html', context)


def result_view(request):
    context = {
        "result": Result.objects.all(),
        "question": Question.objects.all(),
        "user": User.objects.all(),

    }
    return render(request, 'result.html', context)


def result_list_view(request):
    context = {
        "result": Result.objects.all(),
        "user": User.objects.all(),
        "question": Question.objects.all(),
    }
    return render(request, "result-list.html", context)


def user_answer_view(request):
    context = {
        "user_answer": UserAnswer.objects.all(),
    }
    return render(request, "user-answer.html", context)


def calendar_view(request):
    return render(request, 'empty.html')
