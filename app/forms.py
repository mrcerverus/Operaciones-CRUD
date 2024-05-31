from django import forms
from .models import Usuario, Inmueble, SolicitudArriendo
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

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
            'tipo_usuario'
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
        self.helper.add_input(Submit('submit', 'Enviar'))


class SolicitudArriendoForm(forms.ModelForm):
    class Meta:
        model = SolicitudArriendo
        fields = ['inmueble', 'mensaje']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Enviar'))   


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = Usuario
        fields = ['first_name', 'last_name', 'email', 'telefono', 'direccion']
    
    def __init__(self, *args, **kwargs):
        super(UserChangeForm).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Enviar'))