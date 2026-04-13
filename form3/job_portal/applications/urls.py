from django.urls import path
from .views import job_application_view, success

urlpatterns = [
    path('apply/', job_application_view, name='apply'),
    path('success/', success, name='success'),
]