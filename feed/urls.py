from . import views
from django.views.generic.base import TemplateView
from feed.views import main, datboy, nomi
from feed.views import datboy
from django.urls import include, re_path
from django.urls import re_path as url

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.conf import settings
import os

app_name = 'feed'

urlpatterns = [ # main views
    
    re_path('', main.as_view(), name='main'),
    re_path('janye/', views.datboy.as_view(), name='datboy'),
    re_path('nomi/', views.nomi.as_view(), name='nomi'),
    # path('about/', aboutus.as_view(), name='aboutus'),
    
    # path('programs/', programs.as_view(), name='programs'),
    # path('careers/', careers.as_view(), name='careers'),
    
]