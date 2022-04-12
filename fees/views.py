from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def fee_py(req):
      return HttpResponse(3000)

def fee_dj(req):
      return HttpResponse(5000)