from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models
from django.utils import timezone

# from userManagement.managers import CustomUserManager


class CustomUser(AbstractUser):
    nickname = models.CharField(max_length=40, null=True, blank=True)

    def __str__(self):
        return self.email
