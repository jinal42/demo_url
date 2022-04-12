from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def v3(req):
      return HttpResponse("this is view 3...")