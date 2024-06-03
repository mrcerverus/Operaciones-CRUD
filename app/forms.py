from django import forms
from .models import Usuario, Inmueble, SolicitudArriendo, ContactoForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
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

#Formulario de arriendo
class SolicitudArriendoForm(forms.ModelForm):
    class Meta:
        model = SolicitudArriendo
        fields = ['inmueble', 'mensaje']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Enviar'))   

#Formulario edicion de usuario
class UsuarioEditForm(UserChangeForm):
    class Meta:
        model = Usuario
        fields = ['username', 'first_name', 'last_name', 'direccion', 'telefono', 'email']

    def __init__(self, *args, **kwargs):
        super(UsuarioEditForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Guardar cambios'))

#Formulario cambio de password
class CustomPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super(CustomPasswordChangeForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Cambiar Contraseña'))

#Cambiar estado de solicitud de arriendo
class CambiarEstadoSolicitudForm(forms.ModelForm):
    class Meta:
        model = SolicitudArriendo
        fields = ['estado']
        widgets = {
            'estado': forms.Select(attrs={'class': 'form-control'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Cambiar Estado'))

#Formulario de contacto
class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactoForm
        fields = [
            'name',
            'last_name',
            'phone', 
            'email',
            'message'
        ]
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Enviar'))