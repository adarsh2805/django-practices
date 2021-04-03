from django.http import HttpResponse
from django.shortcuts import render
import os

f1=os.path.abspath(__file__)
f2=os.path.dirname(f1)
f3=os.path.join(f2,'sample2.html')

def index(request):
    return HttpResponse('<h1>this is fifth project')

def page1(request):
    return render(request,'sample.html')
def page2(index):
    f5=open(f3,'r')
    file6=f5.read()
    return HttpResponse(file6)