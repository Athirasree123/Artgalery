from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hfun(request):
    return render(request,'demo.html')
def abfun(request):
    return HttpResponse("About Us")