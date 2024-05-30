"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from app.views import index, register, welcome, actualizar_inmueble, crear_inmueble, eliminar_inmueble, detalle_inmueble

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='indice'),
    path('register/', register, name='register'),
    path('bienvenido/', welcome, name='bienvenido'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('inmueble_detalle/', detalle_inmueble , name='detalle_inmueble'),
    path('inmueble_carga/', crear_inmueble, name='cargar_inmueble'),
    path('inmueble_editar/', actualizar_inmueble, name='editar_inmueble'),
    path('inmueble_eliminar/', eliminar_inmueble, name='eliminar_inmueble'),

]

#para cargar imagenes desde base de datos
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)