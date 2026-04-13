from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Home Page
def home(request):
    return render(request, 'home.html')


# Register
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        User.objects.create_user(
            username=username,
            password=password
        )

        return redirect('login')

    return render(request, 'register.html')


# Login
def user_login(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'login.html', {'error': 'Invalid Credentials'})

    return render(request, 'login.html')


# Dashboard
def dashboard(request):

    if request.user.is_authenticated:
        return render(request, 'dashboard.html')
    else:
        return redirect('login')


# Logout
def user_logout(request):
    logout(request)
    return redirect('login')