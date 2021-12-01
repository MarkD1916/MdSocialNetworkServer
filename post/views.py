from django.shortcuts import get_list_or_404
from rest_framework.response import Response
from rest_framework import status, permissions, viewsets
from rest_framework.decorators import api_view, permission_classes, action
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import Post, Like
from .serializers import PostSerializer, LikeSerializer
from rest_framework.pagination import PageNumberPagination


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 5


class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        locker_pk = self.kwargs["post_id"]  # named parameters in url appear in self.kwargs
        return super().get_queryset().filter(post_id=locker_pk)
