from . import views
from django.views.generic.base import TemplateView
from feed.views import nomi, datboy, main
from django.urls import include, re_path, path
from django.urls import re_path as url

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.conf import settings
import os

app_name = 'feed'

urlpatterns = [ # main views
    
    path('', main.as_view(), name='main'),
    path('janye/', datboy.as_view(), name='datboy'),
    path('nomi/', nomi.as_view(), name='nomi'),
    # path('about/', aboutus.as_view(), name='aboutus'),
    
    # path('programs/', programs.as_view(), name='programs'),
    # path('careers/', careers.as_view(), name='careers'),
    
]