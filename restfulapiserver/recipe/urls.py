from django.urls import path, include
from .views import RecipeViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
# 첫 번째 인자는 url의 prefix
# 두 번째 인자는 ViewSet
router.register('recipe', RecipeViewSet)

urlpatterns =[
    path('recipe/', include(router.urls))
]