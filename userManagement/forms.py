from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from userManagement.models import CustomUser


class AuthenticationNewForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = [
            'email',
            'password'
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Please enter your email'})
        self.fields['password'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Please enter your password'})


class UserForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = [
            'email',
            'first_name',
            'last_name',
            'nickname'
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['email'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Please enter your email'})
        self.fields['first_name'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Please enter your first name'})
        self.fields['last_name'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Please enter your last name'})
        self.fields['nickname'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Please enter your nickname'})
        self.fields['password1'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Please enter your password'})
        self.fields['password2'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Please confirm your password'})


class UserUpdateForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = '__all__'
