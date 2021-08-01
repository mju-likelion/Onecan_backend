from rest_framework import serializers
from .models import User

# 데이터를 json형태로 넣어준다


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'phone_number', 'address', 'user_id', 'password']
