from django.db import models
from django.urls import reverse
from categories.models import Category

class Question(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.URLField()
    
    def __str__(self):
        return self.image

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    text = models.CharField(max_length=100, null=True, blank=True)
    is_correct = models.BooleanField()
