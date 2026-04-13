from django.shortcuts import render
import datetime
# Create your views here.
def wish(request):
    time =datetime.datetime.now()
    name='veeresh'
    rollno=100
    marks=85

    formatted_time=time.strftime("%d-%m-%Y %h:%M:%S")
    my_dict = {'insert_date':formatted_time,'name':name, 'rollno':rollno, 'marks':marks }
    return render(request, 'wish.html', my_dict)