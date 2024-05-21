from django.contrib import admin
from app.models import Usuario, Imagen, Inmueble, Region, Comuna
from django.contrib.auth.admin import UserAdmin

# Register your models here.
admin.site.register(Usuario, UserAdmin)
admin.site.register(Inmueble)
admin.site.register(Imagen)
admin.site.register(Region)
admin.site.register(Comuna)
