from django.urls import path
from main.views import *

urlpatterns = [
     path("digital/", digital_view),
     path("direction/", direction_view),
     path('create-user/', create_user),
     path("get-question/", get_question_view),
     path("get_test/", get_test),
     path("create_result/", create_result),
     path("is_logic_directions/", is_logic_directions),
     path('create-user-answer/', create_user_answer),
]


