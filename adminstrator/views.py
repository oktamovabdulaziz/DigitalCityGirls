from django.shortcuts import redirect, render
from django.utils.dateparse import parse_duration
from main.models import *
from adminstrator.forms import QuestionForm, IsLogicQuestionForm
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.models import User


def PagenatorPage(List, num, request):
    paginator = Paginator(List, num)
    pages = request.GET.get("page")
    try:
        list = paginator.page(pages)
    except PageNotAnInteger:
        list = paginator.page(1)
    except EmptyPage:
        list = paginator.page(paginator.num_pages)
    return list


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Foydalanuvchi muvaffaqiyatli kirdi, uning sesiyasini ochamiz
            login(request, user)
            return redirect('index')
        else:
            # Login yoki parol noto'g'ri
            messages.error(request, "Login yoki parolni noto'g'ri kiritdingiz. Iltimos, qaytadan urinib ko'ring!")
            return render(request, 'pages-sign-in.html', {'login_error': True})
    return render(request, 'pages-sign-in.html')


@login_required
def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def reset_password_view(request):
    return render(request, 'pages-reset-password.html')


@login_required
def page_404_view(request):
    return render(request, "pages-404.html")


#  This is Home page view
@login_required
def index_view(request):
    form = QuestionForm
    current_user = request.user
    context = {
        "digital": Digital.objects.all(),
        "forms": form,
        'user': current_user
    }
    return render(request, 'dashboard.html', context)


# This is Directions page view
@login_required
def direction_view(request):
    context = {
        "direction": Direction.objects.all(),
    }
    return render(request, 'direction.html', context)


# This is Create direction page view
@login_required
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


# This is Users list  page view
@login_required
def user_view(request):
    context = {
            "user": User.objects.all(),
        }
    return render(request, "user.html", context)


# This id Digital page view
@login_required
def digital_view(request):
    context = {
        "digital": Digital.objects.all(),
    }
    return render(request, "digital.html", context)


# This is Create Digital view
@login_required
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


# This is Question page view
@login_required
def question_view(request):
    form = QuestionForm
    context = {
        "question": Question.objects.all(),
        "form": form,
    }
    return render(request, "question.html", context)


# This is  edit the question here
@login_required
def question_edit_view(request, pk):
    obj = get_object_or_404(Question, id=pk)

    if request.method == 'GET':
        context = {'form': QuestionForm(instance=obj), 'id': pk}
        return render(request, 'question.html', context)

    if request.method == 'POST':
        form = QuestionForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('direction-by-question', obj.direction.id)
        else:
            context = {'form': form, 'id': pk}
            return render(request, 'question.html', context)


# This is  outputs the result list
@login_required
def result_list_view(request):
    context = {
        "result": Result.objects.all(),
        "user": User.objects.all(),
        "question": Question.objects.all(),
    }
    return render(request, "result-list.html", context)


# This is  outputs the UserAnswer
@login_required
def user_answer_view(request):
    context = {
        "user_answer": UserAnswer.objects.all(),
    }
    return render(request, "user-answer.html", context)


# This is IsLogic page
@login_required
def is_logic_view(request):
    context = {
        "is_logic": IsLogicQuestion.objects.all(),
    }
    return render(request, "is-logic-question.html", context)


# This is  direction selection
@login_required
def select_direction_view(request):
    context = {
        "direction": Direction.objects.all(),
        "questions": Question.objects.all(),
    }
    return render(request, "select-direction.html", context)


# This is  get questions related to direction
@login_required
def direction_by_question_view(request, pk):
    selected_direction = Direction.objects.get(id=pk)
    questions_in_selected_direction = Question.objects.filter(direction=selected_direction)
    paginator = PagenatorPage(questions_in_selected_direction, 3, request)
    return render(request, 'direction-by-question.html', context={'questions': paginator, "dir": pk})




# This is  create question page view
@login_required
def create_question_view(request, pk):
    form = QuestionForm
    formlg = IsLogicQuestionForm
    direction = Direction.objects.get(id=pk)
    context = {
        "form": form,
        "direction": direction,
        "formlg": formlg,

    }
    if request.method == 'GET':
        return render(request, 'create-question.html', context)

    if request.method == 'POST':
        a = Question.objects.create(
            direction=Direction.objects.get(id=pk),
            question=request.POST["question"],
            answer_a=request.POST["answer_a"],
            answer_b=request.POST["answer_b"],
            answer_c=request.POST["answer_c"],
            answer_d=request.POST["answer_d"],
            answer_correct=request.POST["answer_correct"],

          )
        IsLogicQuestion.objects.create(
            direction=Direction.objects.get(id=pk),
            is_logic_question=request.POST["is_logic_question"],
        )

    return redirect("direction-by-question", pk)


@login_required
def save_question_view(request, pk):
    question = Question.objects.get(id=pk)
    if question.is_valid():
        question.save()
    return redirect("direction-by-question")


@login_required
def delete_question_view(request, pk):
    questions = Question.objects.get(id=pk).direction.id
    Question.objects.get(id=pk).delete()
    return redirect('direction-by-question', questions)


