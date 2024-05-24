from django import forms
from .models import Usuario
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

""" class ContactoForm(forms.ModelForm):
    class Meta:
        model = SolicitudArriendo
        fields = [
            'cliente_nombre', 
            'cliente_email', 
            'cliente_telefono', 
            'cliente_direccion', 
            'message', 
            'check_box'
        ]

    def __init__(self, *args, **kwargs):
        super(ContactoForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Enviar')) """

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = [
            'username',
            'password1',
            'password2',
            'rut',
            'first_name',
            'last_name',
            'direccion',
            'email',
            'telefono',
            'tipo_user'
            ]
        
    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Enviar'))