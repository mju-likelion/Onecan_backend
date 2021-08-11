from django.shortcuts import render
from .models import Barter
from .serializers import BarterSerializer
from rest_framework import viewsets

# Barter의 목록, detail 보여주기, 수정하기, 삭제하기 모두 가능
class BarterViewSet(viewsets.ModelViewSet):
    queryset = Barter.objects.all()
    serializer_class = BarterSerializer
    