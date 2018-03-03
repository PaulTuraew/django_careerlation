# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

#codeschool tutorial
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('<h1>Ka..Me..Ha..Me..HAAA!!<h1>')
