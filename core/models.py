from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import User
# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=150)
    email = models.EmailField(unique=True)  # Added unique=True
    phone = models.CharField(max_length=20, blank=True, null=True)
    dob = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)

    def __str__(self):
        return self.user.username
    
    def __str__(self):
        return self.nickname # Corrected to return nickname