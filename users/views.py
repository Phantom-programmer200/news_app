# from rest_framework import generics, status
# from rest_framework.response import Response
# from django.contrib.auth import get_user_model
# from .serializers import UserSerializer
# from django.shortcuts import render, redirect
# from django.contrib.auth import login, authenticate
# from .forms import UserRegisterForm, UserLoginForm
# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# from django.contrib.auth import login, authenticate, logout
# from django.contrib import messages
# from .forms import CustomUserCreationForm


from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
# Ensure this form is defined correctly
from .forms import CustomUserCreationForm

# Registration View


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new user
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'Account created for {username}! You can now log in.')
            # Redirect to the login page after successful registration
            return redirect('login')
        else:
            for error in form.errors.values():
                messages.error(request, error)
    else:
        form = CustomUserCreationForm()

    return render(request, 'register.html', {'form': form})

# Login View


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            # Redirect to a page after successful login
            return redirect('news_page')
        else:
            messages.error(request, 'Invalid username or password.')
            return render(request, 'login.html', {'error': 'Invalid username or password.'})

    return render(request, 'login.html')
