"""MdSocialNetworkServer URL Configuration

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
from authapp.views import index, restricted
from post.views import PostViewSet, LikeViewSet
from userprofile.views import UserProfileViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'post', PostViewSet)
router.register(r'profile', UserProfileViewSet)
router.register(r'(?P<post_id>\d+)like', LikeViewSet, basename='Like')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('checkserver/', index, name='index'),
    path('auth/', include('authapp.urls')),
    path('restricted/', restricted, name='restricted'),
    path('api/', include(router.urls)),
]
