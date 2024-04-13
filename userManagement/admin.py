from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import UserForm, UserUpdateForm
from .models import CustomUser

admin.site.register(CustomUser)
