from rest_framework import serializers
from .models import UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    user_ro = serializers.CharField(source='user.username', read_only=True)

    # author_pk = serializers.CharField(source='author.pk', read_only=True)

    class Meta:
        model = UserProfile
        fields = ['avatar', 'user_ro']
