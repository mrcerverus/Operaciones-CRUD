from itertools import cycle
from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.core.exceptions import ValidationError
import re


# Create your models here.

#Validacion Rut:
def validate_rut(value):
    # Expresión regular para el formato del RUT
    rut_regex = re.compile(r'^\d{1,2}\d{3}\d{3}-[\dkK]$')
    if not rut_regex.match(value):
        raise ValidationError('El RUT debe tener el formato XXXXXXXXX-X')
    
    # Separar el número del dígito verificador
    rut_body, dv = value.split('-')
    rut_body = int(rut_body)
    
    # Calcular el dígito verificador
    reversed_digits = map(int, reversed(str(rut_body)))
    factors = cycle(range(2, 8))
    checksum = sum(d * f for d, f in zip(reversed_digits, factors))
    calculated_dv = (-checksum) % 11
    if calculated_dv == 10:
        calculated_dv = 'K'
    else:
        calculated_dv = str(calculated_dv)
    
    if dv.upper() != calculated_dv:
        raise ValidationError('El RUT no es válido')


class Region(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"Region {self.name}"


class Comuna(models.Model):
    name = models.CharField(max_length=100)
    region = models.ForeignKey(Region, verbose_name="region", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - Region {self.region.name}"


class Usuario(AbstractUser):
    #Propiedades personzalizadas
    TIPO_USER_CHOICES = [
        ('ARRENDADOR', 'arrendador'),
        ('ARRENDATARIO', 'arrendatario'),
    ]

    # nombre = models.CharField(max_length=50)
    # apellido = models.CharField( max_length=50)
    rut = models.CharField(max_length=12, validators=[validate_rut])
    direccion = models.CharField(max_length=50)
    telefono = PhoneNumberField(blank=False, null=False,verbose_name="Telefono de contacto")
    # correo = models.EmailField(max_length=254)
    tipo_user = models.CharField(max_length=20, choices=TIPO_USER_CHOICES, null=False, blank=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.rut} - {self.tipo_user}"


class Inmueble(models.Model):
    TIPO_INMUEBLE_CHOICES = [
        ('CASA', 'Casa'),
        ('DEPARTAMENTO', 'Departamento'),
        ('PARCELA', 'Parcela'),
    ]

    nombre = models.CharField(max_length=200,null=False, blank=False)
    descripcion = models.TextField(null=False, blank=False)
    m2_construidos = models.FloatField(null=False, blank=False)
    m2_totales = models.FloatField(null=False, blank=False)
    cantidad_estacionamientos = models.IntegerField(null=False, blank=False)
    cantidad_habitaciones = models.IntegerField(null=False, blank=False)
    cantidad_banos = models.IntegerField(null=False, blank=False)
    direccion = models.CharField(max_length=200, null=False, blank=False)
    comuna = models.ForeignKey("Comuna", verbose_name="Comuna", on_delete=models.CASCADE)
    tipo_inmueble = models.CharField(max_length=20, choices=TIPO_INMUEBLE_CHOICES, null=False, blank=False)
    precio_mensual_arriendo = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    user = models.ManyToManyField("Usuario", verbose_name="Usuario")
    activo = models.BooleanField(default=True, null=False, blank=False)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Nombre propiedad: {self.nombre} / Fecha Publicacion: {self.fecha_publicacion}"


class Imagen(models.Model):
    inmueble = models.ForeignKey("Inmueble", verbose_name="Inmueble", on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='inmuebles/%Y/%m/%d', null=True, blank=True)

    def __str__(self):
        return f"Imagen de {self.inmueble.nombre}"

class SolicitudArriendo(models.Model):
    TIPO_ESTADO_CHOICES = [
        ('PENDIENTE','Pendiente'),
        ('ACEPTADO','Aceptado'),
        ('RECHAZADO','Rechazado'),
    ]

    arrendatario = models.ForeignKey(Usuario, verbose_name='Usuario', on_delete=models.CASCADE)
    inmueble = models.ForeignKey(Inmueble, on_delete=models.CASCADE)
    mensaje = models.TextField(blank=True)
    estado = models.CharField(choices=TIPO_ESTADO_CHOICES, default='Pendiente')

    def __str__(self):
        return f"Solicitud de {self.inmueble.nombre} por {self.arrendatario.first_name} {self.arrendatario.last_name} "