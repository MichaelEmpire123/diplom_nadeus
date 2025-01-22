from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from .models import CustomUser


class RegistrationForm(UserCreationForm):
    surname = forms.CharField(max_length=255, label='Фамилия')
    name = forms.CharField(max_length=255, label='Имя')
    patronymic = forms.CharField(max_length=255, label='Отчество', required=False)
    phone_number = forms.CharField(max_length=20, label='Телефон')

    class Meta:
        model = CustomUser
        fields = ['surname', 'name', 'patronymic', 'email', 'phone_number', 'password1', 'password2']


class LoginForm(forms.Form):
    username = forms.CharField(label='Логин (почта или телефон)', required=True)
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput, required=True)

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        user = None
        if CustomUser.objects.filter(email=username).exists():
            user = CustomUser.objects.get(email=username)
        elif CustomUser.objects.filter(phone_number=username).exists():
            user = CustomUser.objects.get(phone_number=username)

        if user and authenticate(username=user.username, password=password):
            return cleaned_data

        raise forms.ValidationError("Неверный логин или пароль")
