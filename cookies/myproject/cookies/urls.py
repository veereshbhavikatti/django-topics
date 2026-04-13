from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('set/', views.set_cookie),
    path('get/', views.get_cookie),
    path('delete/', views.delete_cookie),
]