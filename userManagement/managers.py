from django.contrib.auth.base_user import BaseUserManager

# class CustomUserManager(BaseUserManager):
#     # facem asta pentru a lasa doar email in loc de username
#
#     def create_user(self, email, password, **extra_fields):
#         # cream si salvam user-ul cu email si parola
#         if not email:
#             raise ValueError("The email must be set")
#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.save()
#         return user
#
#     def create_superuser(self, email, password, **extra_fields):
#         # pentru crearea de superusers/admins
#         extra_fields.setdefault("is_staff", True)
#         extra_fields.setdefault("is_superuser", True)
#         extra_fields.setdefault("is_active", True)
#
#         if extra_fields.get("is_staff") is not True:
#             raise ValueError("Not superuser, is_staff = False")
#         if extra_fields.get("is_superuser") is not True:
#             raise ValueError("Not superuser, is_superuser = False")
#         return self.create_user(email, password, **extra_fields)
