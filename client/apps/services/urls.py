from django.urls import path, include
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView

from .views import ServicesView


urlpatterns = [
    path('', ServicesView.as_view(), name='services' ),
    path('<slug:slug>', RedirectView.as_view(url='/servicios'), name='services-detail' ),
]