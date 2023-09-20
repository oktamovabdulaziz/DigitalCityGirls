from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


class Digital(models.Model):
    logo = models.ImageField()
    bg_image = models.ImageField()
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Direction(models.Model):
    photo = models.ImageField()
    name = models.CharField(max_length=255)
    time = models.DurationField(default=0)
    question_count = models.PositiveIntegerField()
    is_logic = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class User(models.Model):
    fullname = models.CharField(max_length=255)
    phone = models.PositiveIntegerField()
    direction = models.ForeignKey(Direction, on_delete=models.CASCADE)

    def __str__(self):
        return self.fullname


class Question(models.Model):
    direction = models.ForeignKey(Direction, on_delete=models.CASCADE)
    question = RichTextField()
    answer_a = RichTextUploadingField()
    answer_b = RichTextUploadingField()
    answer_c = RichTextUploadingField()
    answer_d = RichTextUploadingField()
    answer_correct = models.IntegerField(choices=(
        (1, 'a'),
        (2, 'b'),
        (3, 'c'),
        (4, 'd'),
    ))

    def __str__(self):
        return self.question


class IsLogicQuestion(models.Model):
    direction = models.ForeignKey(Direction, on_delete=models.CASCADE, null=False)
    is_logic_question = models.CharField(max_length=255)
    answer = RichTextUploadingField()

    def __str__(self):
        return self.is_logic_question


class Result(models.Model):
    question = models.ForeignKey(Direction, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tru_answers = models.IntegerField()
    false_answers = models.IntegerField()
    total_question = models.IntegerField()
    percentage = models.FloatField()

    def __str__(self):
        return self.user


class UserAnswer(models.Model):
    result = models.ForeignKey(Result, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='question_results')
    answer = models.CharField(max_length=255)
    is_correct = models.BooleanField()


