from django.shortcuts import render
from .models import New_product
from .serializers import New_productSerializer
from rest_framework import viewsets

# Blog의 목록, detail 보여주기, 수정하기, 삭제하기 모두 가능
class New_productViewSet(viewsets.ModelViewSet):
    queryset = New_product.objects.all()
    serializer_class = New_productSerializer