from django.http import HttpResponse

# set cookie
def set_cookie(request):
    response = HttpResponse("Cookie is set")
    response.set_cookie('username', 'Veeresh')
    return response

# get cookie
def get_cookie(request):
    name = request.COOKIES.get('username')
    return HttpResponse(f"Username is {name}")

# delete cookie
def delete_cookie(request):
    response = HttpResponse("Cookie deleted")
    response.delete_cookie('username')
    return response