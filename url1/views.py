from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def v1(req):
      return HttpResponse("this is view 1...")

def v4(req):
      return HttpResponse("this is view 4...")