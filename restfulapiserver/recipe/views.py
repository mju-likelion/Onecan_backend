from django.shortcuts import render
from .models import Recipe
from .serializers import RecipeSerializer
from rest_framework import viewsets

# Recipe의 목록, detail 보여주기, 수정하기, 삭제하기 모두 가능
class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
