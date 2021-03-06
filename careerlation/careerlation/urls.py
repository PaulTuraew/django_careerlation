"""careerlation URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

#codeschool
from careerlationapp import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    
    #localhost/index --> show the index function in views
    #url(r'^index/',
     #  views.index, name='index'),
    
    #localhost/nothing in URL ---> show the home function in views
    url(r'^$', views.home, name='home'),
    
    #localhost/about
    url(r'^about', views.about, name='about'),
    
    #localhost/thesis
    url(r'^thesis', views.thesis, name='thesis'),
    
    #localhost/get-involved
    url(r'^get-involved', views.get_involved, name='get-involved'),
    
]
