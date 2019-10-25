from django.urls import path
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView

from .views import HomeView, PortfolioView, ContactView, \
    QuotationView, ThanksView, SuscribeView, DisplayPDFView, PricePDFView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('brochure', RedirectView.as_view(url='/'), name='brochure'),
    path('brochure_pdf', DisplayPDFView.as_view(), name='brochure_pdf'),
    path('brochure/precios', PricePDFView.as_view(), name='price_pdf'),
    path('cotiza-gratis', QuotationView.as_view(), name='quotation'),
    path('portafolio', PortfolioView.as_view(), name='portfolio'),
    path('contacto', ContactView.as_view(), name='contact'),
    path('mailto', RedirectView.as_view(url='/contacto'), name='mailto'),
    path('suscribe', SuscribeView.as_view(), name='suscribe'),
    path('gracias', ThanksView.as_view(), name='thanks'),
    path('whatsapp', RedirectView.as_view(url='https://wa.me/50762667545'), name='whatsapp'),
    path('go-to-instagram', RedirectView.as_view(url='https://www.instagram.com/asesaludlaboral/'), name='social_instagram'),
    path('go-to-facebook', RedirectView.as_view(url='https://www.facebook.com/asesaludlaboral2727/'), name='social_facebook'),
    path('go-to-twitter', RedirectView.as_view(url='https://www.twitter.com/asesaludlaboral/'), name='social_twitter'),
    path('instagram', RedirectView.as_view(url='/'), name='instagram'),
    path('facebook', RedirectView.as_view(url='/'), name='facebook'),
    path('twitter', RedirectView.as_view(url='/'), name='twitter'),
]