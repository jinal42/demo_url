"""demourl URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django import views
from django.contrib import admin
from django.urls import path,include
from course import views as cv 
from fees import views as fv
# import url1
# from url1 import views as v1
# from url2 import views as v2
# from url3 import views as v3

# from url_1.views import v1,v4


coursepattern=[
        path('cpy/',cv.cou_py),
        path('cdj/',cv.cou_dj),
    ]
feespattern=[
        path('fpy/',fv.fee_py),
        path('fdj',fv.fee_dj),
    ]
    


urlpatterns = [
    # path('u/',include('url1.urls')),  # 'u':route , 'url1':appl. name , 'urls' : url file name of app. (file_name : "urls.py") 


    # path('admin/', admin.site.urls),
    #   path

    # path('v1',v1.v1),
    # path('v4',v1.v4),

    # path('v2',v2.v2),
    # path('v3',v3.v3),
 
    # path('v1',v1),
    # path('v4',v4),
    
    path('url_1/',include('url1.urls')),

    path('c/',include(coursepattern)),
    path('f/',include(feespattern)),
  
    path('c1/',include([
        path('cpy/',cv.cou_py),
        path('cdj/',cv.cou_dj),
   ])),

    path('f/',include([
         path('fpy/',fv.fee_py),
         path('fdj/',fv.fee_dj),
     ]))



]

