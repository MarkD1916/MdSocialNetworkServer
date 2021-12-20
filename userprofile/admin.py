from django.contrib import admin

# Register your models here.
from .models import UserProfile, Relationship
admin.site.register(UserProfile)
admin.site.register(Relationship)