from django.forms import ModelForm
from main.models import *


class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = "__all__"
        exclude = ['direction']


class IsLogicQuestionForm(ModelForm):
    class Meta:
        model = IsLogicQuestion
        fields = "__all__"
        exclude = ['direction']
