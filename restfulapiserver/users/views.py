from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import serializers
from .models import User
from .serializer import UserSerializer
from rest_framework.parsers import JSONParser
# Create your views here.


@csrf_exempt
def login_view(request):
    if request.method == 'GET':
        query_set = User.objects.all()
        serializer = UserSerializer(query_set, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        # client에서 올라온 data를 parsing해서 넣었다
        data = JSONParser().parse(request)
        # 올라온 data랑 우리의 models data랑 포맷이 같으면
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            # 객체를 만든다
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
