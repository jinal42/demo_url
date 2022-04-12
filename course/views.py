from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def cou_py(req):
      return HttpResponse("python course")

def cou_dj(req):
      return HttpResponse("django course")