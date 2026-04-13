from django.contrib import admin
from .models import Employee, HighSalaryEmployee

admin.site.register(Employee)
admin.site.register(HighSalaryEmployee)