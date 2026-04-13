from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# home page 
def home(request):
    return render(request, 'home.html')

# set session
def set_session(request):
    if request.method == 'POST':
        name =request.POST.get('name')
        request.session['username']= name
        return HttpResponse("session stored successfully")
    
        return render(request,'home.html')
    
#get session
def get_session(request):
    name = request.session.get("username")
    return HttpResponse(f"username is {name}")

# delete session

def delete_session(request):
    if 'username' in request.session:
        del request.session['username']
    return HttpResponse("session is deleted")