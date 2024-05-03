from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from userManagement.forms import UserForm, UserUpdateForm
from userManagement.models import CustomUser


class UserCreateView(CreateView):
    template_name = "userManagement/create_user.html"
    model = CustomUser
    form_class = UserForm
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        new_user = form.save(commit=False)
        new_user.email = new_user.email.lower()

        new_user.first_name = new_user.first_name.lower()
        new_user.last_name = new_user.last_name.lower()
        new_user.nickname = new_user.nickname.title()
        # pentru a salva username-ul cu email-ul, did moment ce nu le cerem separat username
        new_user.username = new_user.email

        new_user.save()
        return redirect("login")


class UserUpdateView(UpdateView):
    template_name = "userManagement/update_user.html"
    model = CustomUser
    form_class = UserUpdateForm
    success_url = reverse_lazy("home-page")
