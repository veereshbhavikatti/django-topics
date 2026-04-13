from django.shortcuts import render
from .models import Employee
# Create your views here.

def emloyees(request):
    emp = Employee.objects.all()
    return render(request, 'employees.html',{'emp':emp})
