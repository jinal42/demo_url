from django.urls import path
from url1 import views

urlpatterns=[
      path('v1',views.v1),
      path('v4',views.v4),
]