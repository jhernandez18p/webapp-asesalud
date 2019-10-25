from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Field


class SuscribeForm(forms.Form):

    email = forms.CharField(
        label='Escriba su email',
        widget=forms.TextInput(attrs={'placeholder': 'Email',})
    )


class ContactForm(forms.Form):

    name = forms.CharField(
        label='Escriba su nombre',
        widget=forms.TextInput( attrs = {'placeholder': 'John Doe' } )
    )
    email = forms.CharField(
        label='Escriba su email',
        widget=forms.TextInput(attrs={'placeholder': 'Email',})
    )
    phone = forms.CharField(
        label='Escriba su número de teléfono',
        widget=forms.TextInput(attrs={'placeholder': 'Teléfono'})
    )
    comment = forms.CharField(
        label="Escriba sus comentarios",
        widget=forms.Textarea()
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_action = 'contacto'
        self.helper.layout = Layout(
            Field('name', css_class="form-control"),
            Field('email', css_class='form-control'),
            Field('phone', css_class='form-control'),
            Field('comment', css_class="form-control"),
            Submit('submit', 'Enviar')
        )


class QuotationForm(forms.Form):

    AMOUNT = (
        ('$.','Dolares'),
        ('Bs.','Bolivares'),
        ('unknown','No estoy seguro')
    )
    SERVICES = (
        ('AC','ASESORÍAS Y CAPACITACIONES.'),
        ('EA','EVALUACIONES AMBIENTALES.'),
        ('IA','INVESTIGACIÓN Y ANÁLISIS.'),
        ('DP','DELEGADOS DE PREVENCIÓN.'),
        ('CSSL','COMITÉ DE SEGURIDAD Y SALUD LABORAL.'),
        ('*','OTRO.'),
    )
    name = forms.CharField(
        label='Escriba su nombre',
        widget=forms.TextInput( attrs = {'placeholder': 'John Doe' } )
    )
    email = forms.CharField(
        label='Escriba su email',
        widget=forms.TextInput(attrs={'placeholder': 'Email',})
    )
    phone = forms.CharField(
        label='Escriba su número de teléfono',
        widget=forms.TextInput(attrs={'placeholder': 'Teléfono'})
    )
    country = forms.CharField(
        label="País",
        widget=forms.TextInput(attrs={'placeholder': 'Venezuela'})
    )
    company = forms.CharField(
        label="Nombre de su empresa",
        widget=forms.TextInput(attrs={'placeholder': 'Asesalud Laboral 2727 C.A.'})
    )
    invest = forms.ChoiceField(
        label="Monto de inversión",
        choices=AMOUNT
    )
    subject = forms.ChoiceField(
        label="Tipo de servicio",
        choices=SERVICES
    )
    comment = forms.CharField(
        label="Describa su proyecto",
        widget=forms.Textarea()
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field('name', css_class="form-control"),
            Field('email', css_class='form-control'),
            Field('phone', css_class='form-control'),
            Field('subject', css_class='form-control'),
            Field('country', css_class='form-control'),
            Field('company', css_class='form-control'),
            Field('invest', css_class="form-control"),
            Field('comment', css_class="form-control"),
            Submit('submit', 'Enviar')
        )