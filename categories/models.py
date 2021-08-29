from django.db import models
from django.urls import reverse

class Category(models.Model):
    title = models.CharField(max_length=200)
              
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('cards_list_url', kwargs={'pk': self.pk})

