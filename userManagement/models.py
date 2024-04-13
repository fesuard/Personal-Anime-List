from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from userManagement.managers import CustomUserManager


class CustomUser(AbstractBaseUser):
    # Adding custom fields to the default User model
    email = models.EmailField("email address", unique=True, max_length=60)
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    nickname = models.CharField(max_length=40)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email



