from django.urls import path
from adminstrator.views import *


urlpatterns = [
    path("", login_view, name='login'),
    path("logout/", logout_view, name='logout'),
    path("reset-password/", reset_password_view, name='reset-password'),
    path("page-404/", page_404_view, name='page-404'),
    path("index/", index_view, name='index'),
    path('direction/', direction_view, name="direction"),
    path('create-direction/', create_direction_view, name="create-direction"),
    path("user/", user_view, name='user'),
    path("digital/", digital_view, name='digital'),
    path("create-digital/", create_digital_view, name='create-digital'),
    path("question/", question_view, name='question'),
    path('question-edit/<int:pk>/', question_edit_view, name="edit"),
    path("result-list/", result_list_view, name='result-list'),
    path("is-logic/", is_logic_view, name='is-logic'),
    path("user-answer/", user_answer_view, name='user-answer'),
    path('select-direction/', select_direction_view, name='select-direction'),
    path("direction-by-question/<int:pk>/", direction_by_question_view, name='direction-by-question'),
    path("create-question/<int:pk>/", create_question_view, name='create-question'),
    path("save-question/<int:pk>/", save_question_view, name='save'),
    path("delete-question/<int:pk>/", delete_question_view, name='delete-question'),
]
