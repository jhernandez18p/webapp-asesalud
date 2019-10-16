import os

from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.http import HttpResponse, request
from django.shortcuts import redirect
from django.views import View
from django.views.generic import TemplateView
from django.views.generic.edit import FormView

from server.auth.models import Suscribe
from .forms import ContactForm, QuotationForm, SuscribeForm

"""
Base Views
"""
class HomeView(TemplateView):
    
    template_name = "base/blank.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Inicio'
        context['page_description'] = 'Inicio'
        context['has_banner'] = False
        context['has_aside'] = False
        return context


class ServicesView(TemplateView):
    
    template_name = "base/services.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Servicios'
        context['page_description'] = 'Services'
        context['has_banner'] = True
        context['has_aside'] = True
        return context


class QuotationView(FormView):
    
    template_name = "base/quotation.html"
    success_url = '/gracias'
    form_class = QuotationForm

    def form_valid(self, form):
        self.send_email(form.cleaned_data)
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Cotización gratuita'
        context['page_description'] = 'Cotización gratuita'
        context['has_banner'] = False
        context['has_aside'] = False
        return context

    def send_email(self, valid_data):

        quotation_message = """
        Nombre : {name}               \n
        Email : {email}               \n
        Teléfono : {phone}            \n
        Servicio : {service}          \n
        Monto de inversión : {invest} \n
        Empresa : {company}           \n
        País : {country}              \n
        Comentatios : {comment}
        """.format(
            name=valid_data['name'],
            email=valid_data['email'],
            phone=valid_data['phone'],
            comment = valid_data['comment'],
            invest = valid_data['invest'],
            company = valid_data['company'],
            country = valid_data['country'],
            service = valid_data['subject']
        )

        send_mail(
            subject="Cotización pagina web",
            message=quotation_message,
            from_email='info@dev2tech.xyz',
            recipient_list=['info@dev2tech.xyz',],
        )

        '''
        print(valid_data)
        '''


class PortfolioView(TemplateView):
    
    template_name = "base/portfolio.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Portfolio'
        context['page_description'] = 'Portfolio'
        context['has_banner'] = True
        context['has_aside'] = False
        return context


class BlogView(TemplateView):
    
    template_name = "base/blog.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Blog'
        context['page_description'] = 'Blog'
        context['has_banner'] = True
        context['has_aside'] = False
        return context


class BlogDetailView(TemplateView):
    
    template_name = "base/detail/blog.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Blog'
        context['page_description'] = 'Blog'
        context['has_banner'] = False
        context['has_aside'] = False
        return context


class ContactView(FormView):
    
    template_name = "base/contact.html"
    success_url = '/gracias'
    form_class = ContactForm

    def form_valid(self, form):
        self.send_email(form.cleaned_data)
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Contact'
        context['page_description'] = 'Contact'
        context['has_banner'] = False
        context['has_aside'] = False
        return context

    def send_email(self, valid_data):

        quotation_message = """
        Nombre : {name}               \n
        Email : {email}               \n
        Teléfono : {phone}            \n
        Comentarios : {comment}
        """.format(
            name=valid_data['name'],
            email=valid_data['email'],
            phone=valid_data['phone'],
            comment = valid_data['comment'],
        )

        send_mail(
            subject="Contacto pagina web",
            message=quotation_message,
            from_email='info@dev2tech.xyz',
            recipient_list=['info@dev2tech.xyz',],
        )

        '''
        print(valid_data)
        '''


class SuscribeView(FormView):
    
    template_name = "base/suscribe.html"
    success_url = '/gracias'
    form_class = SuscribeForm

    def post(self, request):

        if request.POST['email']:
            # print(request.POST)
            email = request.POST['email']
            subscriber = Suscribe(email=email)
            subscriber.save()
            self.send_email(email)
        
        return super().form_valid(SuscribeForm)

    def form_valid(self, form):
        self.send_email(form.cleaned_data)
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Gracias por suscribirse'
        context['page_description'] = 'Ud. se ha suscrito a nuestra lista contactos.'
        context['has_banner'] = False
        context['has_aside'] = True
        return context

    def send_email(self, email):

        suscribe_message = """
        Email : {email}               \n
        """.format(
            email=email,
        )

        send_mail(
            subject="Suscriptor página web",
            message=suscribe_message,
            from_email='info@dev2tech.xyz',
            recipient_list=['info@dev2tech.xyz',],
        )

        '''
        print(valid_data)
        '''


class ThanksView(TemplateView):
    
    template_name = "base/thanks.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Gracias'
        context['page_description'] = 'Ud. se ha comunicado con el equipo de Dev2tech, su solicitud será procesada en breve.'
        context['has_banner'] = False
        context['has_aside'] = True
        return context


class DisplayPDFView(View):

    def get_context_data(self, **kwargs):
        context = {}
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        base_path = os.path.join(os.path.join(os.path.dirname(settings.BASE_DIR), "staticfiles"), 'pdf')
        path = os.path.join(base_path, 'brochure.pdf')
        try:
            with open(path, 'rb') as pdf:
                response = HttpResponse(pdf.read(),content_type='application/pdf')
                response['Content-Disposition'] = 'filename="brochure.pdf"'
            pdf.closed

        except:
            response = redirect('/contacto')

        return response


class PricePDFView(View):

    def get_context_data(self, **kwargs):
        context = {}
        return context

    def get(self, request, *args, **kwargs):   
        context = self.get_context_data()
        base_path = os.path.join(os.path.join(os.path.dirname(settings.BASE_DIR), "staticfiles"), 'pdf')
        path = os.path.join(base_path, 'precios.pdf')
        try:
            with open(path, 'rb') as pdf:
                response = HttpResponse(pdf.read(),content_type='application/pdf')
                response['Content-Disposition'] = 'filename="precios.pdf"'
            pdf.closed

        except:
            response = redirect('/contacto')

        return response


def mailto_view(request):
    response = redirect('/contacto')
    return response