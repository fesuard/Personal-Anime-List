import django
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.forms import TextInput

from userManagement.models import CustomUser


class AuthenticationNewForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = [
            'username',
            'password'
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # username_field: django.contrib.auth.forms.UsernameField = self.fields['username']
        username_field = self.fields['username']
        username_field.label = 'Email'
        self.fields['username'].widget.attrs.update(
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

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        if email is None or email == '':
            raise forms.ValidationError('Email is mandatory')
        user = CustomUser.objects.filter(email=email).first()
        if user is not None:
            raise forms.ValidationError('This email is already in use')

        return email


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'nickname']

        widgets = {
            'first_name': TextInput(attrs={'class': 'form-control'}),
            'last_name': TextInput(attrs={'class': 'form-control'}),
            'nickname': TextInput(attrs={'class': 'form-control'}),

        }