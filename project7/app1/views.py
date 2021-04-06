from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('<center><h1 style="background-color:grey">httpresponse of apps1 project7</h1></center>')

def sample(request):
    return render(request,'sample_app1.html')
def carry_url(request,data):
    return HttpResponse(f'<center><h1>you entered {data}</h1></center>')

def fact(request,num):
    a=int(num)
    b=1
    for i in range(int(num),1,-1):
        b*=i
    return HttpResponse(f'{b}')
    

