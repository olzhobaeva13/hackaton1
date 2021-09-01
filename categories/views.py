from cards.serializers import QuestionSerializer
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from .models import Category
from .serializers import CategorySerializer
from cards.models import Question
from rest_framework import status


# class CategoryAPIView(APIView):
#     def get(self, request):
#         categories = Category.objects.all()
#         serializer = CategorySerializer(categories, many=True)
#         return Response(serializer.data)

class CategoriesListVIew(ListAPIView):
    serializer_class = CategorySerializer
    def get_queryset(self):
        return Category.objects.all()

class CategoryListAPIView(ListAPIView):
    serializer_class = QuestionSerializer
    def get_queryset(self):
        return Question.objects.filter(category_id=self.kwargs.get('category_id'))
    

class CardAPIView(APIView):
    def get(self, request):
        questions = Question.objects.all()
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = QuestionSerializer(data=request.data)

        if serializer.is_valid():
            category = serializer.validated_data.get('category')
            image = serializer.validated_data.get('image')
            answers = serializer.validated_data.get('answers')
            question = Question.objects.create(category=category, image = image, answers=answers)
            serializer = QuestionSerializer(instance=question)

            return Response(serializer.data)
        return Response({'detail': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
