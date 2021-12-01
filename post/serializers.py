from django.db.models import Count
from rest_framework import serializers
from .models import Post, Like

class LikeSerializer(serializers.ModelSerializer):
    author_ro = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Like
        fields = ['post', 'author_ro', 'user']

class PostSerializer(serializers.ModelSerializer):
    author_ro = serializers.CharField(source='author.username', read_only=True)
    likes_count = serializers.IntegerField(
        source='likes.count',
        read_only=True
    )
    class Meta:
        model = Post
        fields = ['pk', 'post_title', 'author_ro', 'author', 'post_text_content', 'post_image', 'post_date', 'likes_count']




