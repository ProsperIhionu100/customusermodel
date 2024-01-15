from django.db import models

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200,unique=True)
    bio = models.TextField(null=True)
    location = models.CharField(max_length=200, null=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []