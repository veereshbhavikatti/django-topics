from django.shortcuts import render
from .models import HighSalaryEmployee

def high_salary_employees(request):

    employees = HighSalaryEmployee.objects.all()

    return render(request, 'employees.html', {'employees': employees})