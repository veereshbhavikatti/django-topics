# from django.shortcuts import render
from django.http import HttpResponse


def messages(request):
    s= " hi my name is veeresh" # Create your views here.
    return HttpResponse(s)