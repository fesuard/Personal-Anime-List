from django.contrib.auth.models import PermissionsMixin, AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    nickname = models.CharField(max_length=40, null=True, blank=True)

    def __str__(self):
        return self.email



