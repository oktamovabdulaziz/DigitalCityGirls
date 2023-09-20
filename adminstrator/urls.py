from django.urls import path, re_path, include
from adminstrator.views import *
from adminstrator.forms import QuestionForm

urlpatterns = [
    path("", index_view, name='index'),
    path('direction/', direction_view, name="direction"),
    path('create-direction/', create_direction_view, name="create-direction"),
    path("user/", user_view, name='user'),
    path("digital/", digital_view, name='digital'),
    path("create-digital/", create_digital_view, name='create-digital'),
    path("question/", question_view, name='question'),
    path("question-list/", question_list_view, name='question-list'),
    path('question-edit/<int:pk>/', question_edit_view, name="edit"),
    path("create-question/", create_question_view, name='create-question'),
    path("result-list/", result_list_view, name='result-list'),
    path("user-answer/", user_answer_view, name='user-answer'),
    path('yo`nalishlar/<int:direction_id>/', direction_questions, name='select-direction'),

]
