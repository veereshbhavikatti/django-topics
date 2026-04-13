from django.shortcuts import render
from .models import Employee
# Create your views here.

def employee_view(request):
    emp_data= Employee.objects.all()
    return render(request, 'home.html',{'emp_data' : emp_data})
