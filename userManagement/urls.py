from django.urls import path

from userManagement import views

urlpatterns = [
    path("create_user/", views.UserCreateView.as_view(), name="create-user"),
    path("update_user/<int:pk>/", views.UserUpdateView.as_view(), name="update-user"),
]
