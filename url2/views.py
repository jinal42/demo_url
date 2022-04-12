from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def v2(req):
      return HttpResponse("this is view 2...")
def v5(req):
      return HttpResponse("this is view 5...")


      