from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name="user_in_profile", on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='event_icons/', default='prod_default_image.png')
# Create your models here.
