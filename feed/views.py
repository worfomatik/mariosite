# from django.shortcuts import render
# from django.views import View
# from django.shortcuts import render, get_object_or_404
# from django.core.mail import send_mail, BadHeaderError, EmailMessage
# from django.http import HttpResponse, HttpResponseRedirect
# from django.views.generic import TemplateView
# from django.shortcuts import render, redirect
# import os

from django.shortcuts import render, get_object_or_404
from django.core.mail import send_mail, BadHeaderError, EmailMessage
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
# from .forms import ContactForm
from django.views.generic import TemplateView
from django.views import View
from django.conf import settings
import os
# from .models import Message
# from urllib import request

# from sentry_sdk import capture_exception
class datboy(View):
    # form_class = ContactForm
    initial = {'key': 'value'}
    template_name = 'feed/datboy.html'
    

    def get(self, request, *args, **kwargs):
        # form = self.form_class(initial=self.initial)
        # return render(request, self.template_name, {'form': form})
        print("datboy views function is at least called")
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        
        # return render(request, self.template_name, {'form': form})
        return render(request, self.template_name)
        
class main(View):
    # form_class = ContactForm
    initial = {'key': 'value'}
    template_name = 'feed/main.html'
    print("maion views function is at least called")

    def get(self, request, *args, **kwargs):
        # form = self.form_class(initial=self.initial)
        # return render(request, self.template_name, {'form': form})
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        
        # return render(request, self.template_name, {'form': form})
        return render(request, self.template_name)

class nomi(View):
    # form_class = ContactForm
    initial = {'key': 'value'}
    template_name = 'feed/nomi.html'

    def get(self, request, *args, **kwargs):
        # form = self.form_class(initial=self.initial)
        # return render(request, self.template_name, {'form': form})
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        
        # return render(request, self.template_name, {'form': form})
        return render(request, self.template_name)

