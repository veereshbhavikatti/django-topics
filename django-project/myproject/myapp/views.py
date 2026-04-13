# from django.shortcuts import render
from django.http import HttpResponse
# # Create your views here.

def display(request):
    s ="<h1> hello ,students welcome to django class</h1>"
    return HttpResponse(s)