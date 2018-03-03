# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

#codeschool tutorial
from django.http import HttpResponse

# Create your views here.

#codeschool tutorial
#def index(request):
 #   return HttpResponse('<h1>This is the Index page</h1>')

#mike hibbert's tutorial
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def thesis(request):
    return render(request, 'thesis.html')

def get_involved(request):
    return render(request, 'get-involved.html')

