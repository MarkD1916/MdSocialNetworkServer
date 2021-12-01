from rest_framework.response import Response
from rest_framework import status, permissions, viewsets
from rest_framework.decorators import api_view, permission_classes, action
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import UserProfile
from .serializers import UserProfileSerializer


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

    # def get_permissions(self):
    #     if self.action == 'list':
    #         return [IsAdminUser()]
    #     else:
    #         return super(self, PostViewSet).get_permissions()
