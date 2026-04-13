from django.urls import path
from . import views

urlpatterns = [

    path('setcookie/', views.set_cookie),
    path('getcookie/', views.get_cookie),
    path('deletecookie/', views.delete_cookie),

]