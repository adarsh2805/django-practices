from django.http import HttpResponse
import os

n1=os.path.abspath(__file__)
n2=os.path.dirname(n1)
n3=os.path.join(n2,'sample.html')

def index(request):
    f1=open(n3,'r')
    f2=f1.read()
    return HttpResponse(f2)