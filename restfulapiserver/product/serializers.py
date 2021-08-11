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

from .models import Product
from rest_framework import serializers


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
