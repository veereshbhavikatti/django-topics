
from django.urls import path
from . import views

urlpatterns = [
    path("employees/", views.Employee, name="employees"),
]