from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    birth_date = forms.DateField( widget=forms.SelectDateWidget( empty_label=("Dia", "Mes", "Año"),)) #validators=[validate_date])
    avatar = forms.FileField()  

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'avatar', 'birth_date', 'email', 'password1', 'password2', )