from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import serializers
from .models import User
from .serializer import UserSerializer
from rest_framework.parsers import JSONParser
from django.contrib import auth
# Create your views here.


