from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import RegistrationForm, LoginForm
from django.contrib.auth.decorators import login_required
from .models import CustomUser


def home(request):
    return render(request, 'almet/index.html')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'auth/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = None
            if CustomUser.objects.filter(email=username).exists():
                user = CustomUser.objects.get(email=username)
            elif CustomUser.objects.filter(phone_number=username).exists():
                user = CustomUser.objects.get(phone_number=username)

            if user:
                login(request, user)
                return redirect('profile')
    else:
        form = LoginForm()

    return render(request, 'auth/login.html', {'form': form})


@login_required
def profile(request):
    return render(request, 'auth/profile.html', {'user': request.user})


def logout_view(request):
    logout(request)
    return redirect('home')
