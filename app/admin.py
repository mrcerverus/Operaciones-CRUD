from django.contrib import admin
from app.models import Usuario, Inmueble, Region, Comuna, SolicitudArriendo, ContactoForm
from django.contrib.auth.admin import UserAdmin

admin.site.site_header = 'Administracion Sitio Arriendos'
admin.site.index_title = 'Panel De Control'
admin.site.site_title = 'Arriendos'

class UserAdmin(UserAdmin):
    resource_class = Usuario
    list_display = ['username','rut','first_name','last_name','email', 'tipo_usuario', 'is_staff']
    fieldsets = UserAdmin.fieldsets + (
        ('Datos', {'fields': ('rut', 'direccion', 'telefono', 'tipo_usuario')}),
    )


# Register your models here.

admin.site.register(Usuario, UserAdmin)
admin.site.register(Inmueble)
admin.site.register(Region)
admin.site.register(Comuna)
admin.site.register(SolicitudArriendo)
admin.site.register(ContactoForm)