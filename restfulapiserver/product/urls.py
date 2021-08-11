# from django.conf.urls import url
# from . import views


# urlpatterns = [
#      url(r'(?P<pk>[0-9]+)/', views.CartDetail.as_view(), name='detail'),
#     #url(r'<int:pk>/', views.MovieDetail.as_view()) # 정규표현식 에러
#     url(r'', views.CartList.as_view(), name='carts')
# ]

from django.urls import path, include
from .views import ProductViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
# 첫 번째 인자는 url의 prefix
# 두 번째 인자는 ViewSet
router.register('product', ProductViewSet)

urlpatterns = [
    path('', include(router.urls))
]

# from django.urls import path
# from .views import CartViewSet

# # Blog 목록 보여주기
# cart_list = CartViewSet.as_view({
#     'get': 'list',
#     'post': 'create'
# })

# # Blog detail 보여주기 + 수정 + 삭제
# cart_detail = CartViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'delete': 'destroy'
# })

# urlpatterns =[
#     path('cart/', cart_list),
#     path('cart/<int:pk>/', cart_detail),
# ]
