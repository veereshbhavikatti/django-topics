from django.shortcuts import render
from django.http import HttpResponse

# Home Page
def home(request):
    return render(request, 'home.html')

# Set Cookie
def set_cookie(request):
    response = HttpResponse("Cookie Set Successfully")
    response.set_cookie('username', 'Veeresh')
    return response

# Get Cookie
def get_cookie(request):
    name = request.COOKIES.get('username')
    return HttpResponse(f"Username is: {name}")

# Delete Cookie
def delete_cookie(request):
    response = HttpResponse("Cookie Deleted")
    response.delete_cookie('username')
    return response