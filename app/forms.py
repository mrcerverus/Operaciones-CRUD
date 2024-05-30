from django import forms
from .models import Usuario, Inmueble
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

#Formulario Creacion de Usuario
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

#Formulario Inmueble
class InmuebleForm(forms.ModelForm):
    class Meta:
        model = Inmueble
        fields = [
            'nombre',
            'descripcion',
            'm2_construidos',
            'm2_totales',
            'cantidad_estacionamientos',
            'cantidad_habitaciones',
            'cantidad_banos',
            'direccion',
            'comuna',
            'tipo_inmueble',
            'precio_mensual_arriendo',
            'activo',
            'imagen',
        ]

        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Cargar Cambios'))