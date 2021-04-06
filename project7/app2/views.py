from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('<center><h1 style="background-color:grey">httpresponse of apps2</h1></center>')
    
def sample(request):
    return render(request,'sample_app2.html')