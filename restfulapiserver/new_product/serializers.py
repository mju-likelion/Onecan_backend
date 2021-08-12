from .models import New_product
from rest_framework import serializers

class New_productSerializer(serializers.ModelSerializer):
    class Meta:
        model = New_product
        fields = '__all__'