# from rest_framework import serializers
# from cart.models import Cart


# class CartSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Cart
#         # fields = ['id','product_name', 'price']
#         fields = (
#             'id',
#             'title',
#             'subtitle',
#             'content',
#             'created_at',
#         )
#         read_only_fields = ('created_at',)

from .models import Cart
from rest_framework import serializers

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'
