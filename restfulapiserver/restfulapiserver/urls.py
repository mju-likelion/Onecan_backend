"""restfulapiserver URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url, include
from users import views
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     url(r'^api-auth', include('rest_framework.urls'))
# ]
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('login/', views.login_view),
    # path('signup/', views.signup_view),
    # path('logout', views.logout_view),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
]
