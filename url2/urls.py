from django.urls import path
from url2 import views                 #  from . import views

urlpatterns=[
      path('v2',views.v2),
      path('v5',views.v5),
      
]