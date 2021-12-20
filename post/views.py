from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from userprofile.models import UserProfile
from .models import Post, Like
from .serializers import PostSerializer, LikeSerializer
from django.db.models import OuterRef, Subquery
from rest_framework.response import Response


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 3


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        user_pk = self.request.user.pk
        # print (user_pk)
        # my_post = UserProfile.objects.filter(user=user_pk) # MY_POST

        friends_post = UserProfile.objects.filter(user=user_pk).values_list('friends', flat=True)
        print(list(friends_post))
        return super().get_queryset().filter(author__in=list(friends_post))


class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        locker_pk = self.kwargs["post_id"]  # named parameters in url appear in self.kwargs
        return super().get_queryset().filter(post_id=locker_pk)
