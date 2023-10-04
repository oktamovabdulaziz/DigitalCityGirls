from .serializer import *
from rest_framework.decorators import api_view
from rest_framework.generics import *
from rest_framework.response import Response
from .models import *
from rest_framework import status
from django.shortcuts import get_object_or_404


# This is Get Digital view
@api_view(["GET"])
def digital_view(request):
    digit = Digital.objects.all()
    data = DigitalSerializer(digit, many=True).data
    return Response({"data": data})


# This is Get Direction view
@api_view(["GET"])
def direction_view(request):
    direction = Direction.objects.all()
    data = DirectionSerializer(direction, many=True).data
    return Response({"data": data})


# This is Get IsLogicDirection view
@api_view(['GET'])
def is_logic_directions_view(request):
    is_logic_direction = Direction.objects.filter(is_logic=True)
    serializer = DirectionSerializer(is_logic_direction, many=True)
    return Response(serializer.data)


# This is Get test view
@api_view(['GET'])
def get_test_view(request):
    try:
        user_id = request.GET["user_id"]
        user = User.objects.get(id=user_id)
        choising_test = Question.objects.filter(direction=user.direction).order_by("?")[user.direction.question_count]
        ser = QuestionSerializer(choising_test, many=True).data
        return Response({"data": ser})
    except Exception as err:
        return Response({"success": f"{err}"})


# This is Create User view
@api_view(['POST'])
def create_user_view(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# This is Get Question view
@api_view(['GET'])
def get_question_view(request):
    query = Question.objects.all()
    data = QuestionSerializer(query, many=True).data
    return Response({"data": data})


# This is Create Result view
@api_view(['GET', 'POST'])
def create_result_view(request):
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


# This is Create UserAnswer view
@api_view(['POST'])
def create_user_answer_view(request):
    if request.method == 'POST':
        serializer = UserAnswerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# This is Get IsLogicQuestion view
@api_view(['GET'])
def get_is_logic_questions_view(request, direction_id):
    try:
        direction = Direction.objects.get(id=direction_id)
    except Direction.DoesNotExist:
        return Response({'message': 'Direction not found'}, status=404)

    if direction.is_logic:
        is_logic_questions = IsLogicQuestion.objects.filter(direction=direction)
        serializer = IsLogicQuestionSerializer(is_logic_questions, many=True)
        return Response(serializer.data)
    else:
        return Response({'message': 'This direction does not have logic questions'}, status=400)
