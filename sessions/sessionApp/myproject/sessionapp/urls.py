from django.urls import path
from . import views

urlpatterns = [

    path('', views.home),
    path('set/', views.set_session),
    path('get/', views.get_session),
    path('delete/', views.delete_session),

]