from django.urls import path
from main.views import *

urlpatterns = [
     path("digital/", digital_view, name='digital'),
     path("direction/", direction_view, name='get-direction'),
     path('create-user/', create_user_view, name='create-user'),
     path("get-question/", get_question_view, name='get-question'),
     path("get_test/", get_test_view, name='get-test'),
     path("create_result/", create_result_view, name='create-result'),
     path("is_logic_directions/", is_logic_directions_view, name='is-logic-direction'),
     path('create-user-answer/', create_user_answer_view, name='create-user-answer'),
     path('directions/<int:direction_id>/is-logic-questions/', get_is_logic_questions_view, name='get-is-logic-questions'),

]


