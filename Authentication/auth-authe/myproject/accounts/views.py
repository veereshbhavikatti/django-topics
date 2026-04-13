from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'home.html')


@login_required
def dashboard(request):

    if request.user.is_superuser:
        return redirect('admin_dashboard')

    elif request.user.groups.filter(name='Teacher').exists():
        return redirect('teacher_dashboard')

    elif request.user.groups.filter(name='Student').exists():
        return redirect('student_dashboard')

    else:
        return render(request, 'dashboard.html')


@login_required
def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')


@login_required
def teacher_dashboard(request):
    return render(request, 'teacher_dashboard.html')


@login_required
def student_dashboard(request):
    return render(request, 'student_dashboard.html')