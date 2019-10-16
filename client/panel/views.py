from django.http import HttpResponse
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


"""
Dashboard View
"""
class DashboardView(LoginRequiredMixin ,TemplateView):
    template_name = "home.html"