# from .models import Cart
# from django.http import Http404
# from rest_framework import status
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from .serializers import CartSerializer

# # Create your views here.

# class CartList(APIView):
#     # """
#     #     카트 리스트 생성
#     # """
#     def post(self, request, format=None):
#         serializer = CartSerializer(data=request.data)
#         if serializer.is_valid() :
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
#     #   """
#     #     카트 리스트 조회
#     #   """
#     def get(self, request, format=None):
#         queryset = Cart.objects.all()
#         serializer = CartSerializer(queryset, many=True)
#         return Response(serializer.data)

# class CartDetail(APIView) :
#     def get_object(self, pk):
#         try :
#             return Cart.objects.get(pk=pk)
#         except :
#             raise Http404
 
#     def get(self, request, pk):
#         cart = self.get_object(pk)
#         serializer = CartSerializer(cart)
#         return Response(serializer.data)
 
#     def put(self, request, pk, format=None):
#         cart = self.get_object(pk)
#         serializer = CartSerializer(cart, data=request.data)
#         if serializer.is_valid() :
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
#     def delete(self, request, pk, format=None):
#         cart = self.get_object(pk)
#         cart.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

from .models import Cart
from .serializers import CartSerializer
from rest_framework import viewsets

# Blog의 목록, detail 보여주기, 수정하기, 삭제하기 모두 가능
class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer