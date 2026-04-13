from django.urls import path
from . import views

urlpatterns = [
    path('high-salary/', views.high_salary_employees),
]