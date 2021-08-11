from .models import Barter
from rest_framework import serializers

class BarterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Barter
        fields = '__all__'