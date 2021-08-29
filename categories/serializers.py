from rest_framework import serializers
from .models import Category
from django.db.models import fields

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','title']

