from .serializer import *
from rest_framework.decorators import api_view
from rest_framework.generics import *
from rest_framework.response import Response
from .models import *
from rest_framework import status
from django.shortcuts import get_object_or_404


@api_view(["GET"])
def digital_view(request):
    digit = Digital.objects.all()
    data = DigitalSerializer(digit, many=True).data
    return Response({"data": data})


@api_view(["GET"])
def direction_view(request):
    direction = Direction.objects.all()
    data = DirectionSerializer(direction, many=True).data
    return Response({"data": data})


@api_view(['GET'])
def is_logic_directions(request):
    is_logic_direction = Direction.objects.filter(is_logic=True)
    serializer = DirectionSerializer(is_logic_direction, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_test(request):
    try:
        user_id = request.GET["user_id"]
        user = User.objects.get(id=user_id)
        choising_test = Question.objects.filter(direction=user.direction).order_by("?")[user.direction.question_count]
        ser = QuestionSerializer(choising_test, many=True).data
        return Response({"data": ser})
    except Exception as err:
        return Response({"success": f"{err}"})


@api_view(['POST'])
def create_user(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_question_view(request):
    query = Question.objects.all()
    data = QuestionSerializer(query, many=True).data
    return Response({"data": data})


@api_view(['GET', 'POST'])
def create_result(request):
    if request.method == 'GET':
        results = Result.objects.all()
        serializer = ResultSerializer(results, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ResultSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED,)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def create_user_answer(request):
    if request.method == 'POST':
        serializer = UserAnswerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def create_is_logic_question_view(request):
    is_logic = IsLogicQuestion.objects.all()
    serializer = IsLogicQuestionSerializer(is_logic, many=True).data
    return Response({"data": serializer})
