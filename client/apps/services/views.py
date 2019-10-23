import os

from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.http import HttpResponse, request
from django.shortcuts import redirect
from django.views import View
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.shortcuts import render

# Create your views here.

class ServicesView(TemplateView):
    
    template_name = "base/services.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Servicios'
        context['page_description'] = 'Services'
        context['has_banner'] = True
        context['has_aside'] = True
        return context
