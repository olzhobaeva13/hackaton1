from rest_framework import serializers
from .models import Question, Answer
from django.db.models import fields

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['id', 'text']

class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True)
    category = serializers.CharField(source='category.title')
    class Meta:
        model = Question
        fields = ['id', 'category', 'image', 'answers']

