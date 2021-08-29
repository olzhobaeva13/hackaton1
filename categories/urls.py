from django.urls import path
from .views import CategoriesListVIew, CategoryListAPIView, CardAPIView


urlpatterns = [
    path('categories', CategoriesListVIew.as_view(), name='categories_list_url'),
    path('categories/<int:category_id>/',CategoryListAPIView.as_view()),
    path('cards/', CardAPIView.as_view(), name='cards_list_url'),
]