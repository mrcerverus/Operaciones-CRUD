from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request,'index.html', {})

def about(request):
    return render(request,'about.html', {})

#detalle del inmueble
@login_required
def detalle_inmueble(request, id):
    inmueble = Inmueble.objects.get (pk=id)
    return render(request,'detalle_inmueble.html',{'inmueble':inmueble})

#Formulario de registro
def register(request):
    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        user_creation_form = CustomUserCreationForm(data=request.POST)
        if user_creation_form.is_valid():
            user_creation_form.save()
            usuario = authenticate(username=user_creation_form.cleaned_data['username'], password=user_creation_form.cleaned_data['password1'])
            login(request, usuario)
            return redirect('indice')
        else:
            data['form'] = user_creation_form

    return render(request, 'registration/register.html', data)

#Generar solicitud de arriendo
@login_required
def generar_solicitud_arriendo(request, id):
    # Obtener el inmueble por su ID
    inmueble = get_object_or_404(Inmueble, pk=id)
    
    # Verificar si el usuario está autenticado y es un arrendatario
    if request.user.is_authenticated and request.user.tipo_usuario == 'ARRENDATARIO':
        if request.method == 'POST':
            form = SolicitudArriendoForm(request.POST)
            if form.is_valid():
                solicitud = form.save(commit=False)
                solicitud.arrendatario = request.user  # Asignar el usuario arrendatario
                solicitud.inmueble = inmueble
                solicitud.save()
                return redirect('detalle_inmueble', id=inmueble.id)
        else:
            # Inicializar el formulario con el inmueble correspondiente
            form = SolicitudArriendoForm(initial={'inmueble': inmueble})
        return render(request, 'generar_solicitud_arriendo.html', {'form': form})
    else:
        return redirect('index')

#Solicitudes Arrendedor
@login_required
def solicitudes_arrendador(request):
    # Verificar si el usuario es un arrendador
    if request.user.tipo_usuario == 'ARRENDADOR':
        # Obtener todas las solicitudes recibidas por el arrendador
        solicitudes = SolicitudArriendo.objects.filter(inmueble__propietario=request.user)
        return render(request, 'solicitudes_arrendador.html', {'solicitudes': solicitudes})
    else:
        # Redirigir a otra página si el usuario no es un arrendador
        return redirect('indice')

#Solicitudes Arrendatario
@login_required
def solicitudes_arrendatario(request):
    if request.user.tipo_usuario == 'ARRENDATARIO':
        solicitudes = SolicitudArriendo.objects.filter(arrendatario=request.user)
    return render(request, 'solicitudes_arrendatario.html', {'solicitudes': solicitudes})

#Crear Inmueble
@login_required
def crear_inmueble(request):
    if request.method == 'POST':
        form = InmuebleForm(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            inmueble = form.save(commit=False)
            inmueble.propietario = request.user
            inmueble.save()
            #message = "Inmueble Creado De Forma Exitosa"
            return redirect('welcome') 
    else:
        form = InmuebleForm()
    return render(request, 'registration/cargar_inmueble.html', {'form': form})

#Actualizar Inmuebles
@login_required
def actualizar_inmueble(request, id):
    inmueble = get_object_or_404(Inmueble, pk=id)
    if request.method == 'POST':
        form = InmuebleForm(request.POST, request.FILES, instance=inmueble)
        if form.is_valid():
            form.save()
            return redirect('welcome')
    else:
        form = InmuebleForm(instance=inmueble)
    return render(request, 'registration/actualizar_inmueble.html', {'form': form})

#Eliminar Inmueble
@login_required
def eliminar_inmueble(request, id):
    inmueble = get_object_or_404(Inmueble, pk=id)
    if request.method == 'POST':
        inmueble.delete()
        return redirect('welcome')
    else:
        return render(request,'registration/eliminar_inmueble.html', {'inmueble':inmueble} )

#Muestra inmuebles segun login
@login_required
def welcome(request):
    if request.user.tipo_usuario == 'ARRENDATARIO':
        solicitudes = SolicitudArriendo.objects.filter(arrendatario=request.user)
        regiones = Region.objects.all()
        comunas = Comuna.objects.all()
        region_id = request.GET.get('region')
        comuna_id = request.GET.get('comuna')
        inmuebles = Inmueble.objects.all()
        if region_id:
            inmuebles = inmuebles.filter(comuna__region_id=region_id)
        if comuna_id:
            inmuebles = inmuebles.filter(comuna_id=comuna_id)
        
        return render(request, 'welcome_arrendatario.html', {'solicitudes': solicitudes, 'regiones': regiones, 'comunas': comunas, 'inmuebles': inmuebles})
    
    elif request.user.tipo_usuario == 'ARRENDADOR':
        # Obtener las solicitudes recibidas por el arrendador
        solicitudes_enviadas = SolicitudArriendo.objects.filter(inmueble__propietario=request.user)
        # Obtener los inmuebles del arrendador
        inmuebles = Inmueble.objects.filter(propietario=request.user)
        # Obtener regiones y comunas para el filtro
        regiones = Region.objects.all()
        comunas = Comuna.objects.all()
        region_id = request.GET.get('region')
        comuna_id = request.GET.get('comuna')
        if region_id:
            inmuebles = inmuebles.filter(comuna__region_id=region_id)
        if comuna_id:
            inmuebles = inmuebles.filter(comuna_id=comuna_id)

        context = {
            'solicitudes_enviadas': solicitudes_enviadas,
            'inmuebles': inmuebles,
            'regiones': regiones,
            'comunas': comunas,
        }

        return render(request, 'welcome_arrendador.html', context)


#cambiar estado de solicitud
@login_required
def cambiar_estado_solicitud(request, id):
    solicitud = get_object_or_404(SolicitudArriendo, pk=id)
    if request.method == 'POST':
        form = CambiarEstadoSolicitudForm(request.POST, request.FILES, instance=solicitud)
        if form.is_valid():
            form.save()
            return redirect('solicitudes_arrendador')
    else:
        form = CambiarEstadoSolicitudForm(instance=solicitud)
    return render(request, 'registration/cambiar_estado_solicitud.html', {'form': form})

#Actualizar Usuario
@login_required
def editar_usuario(request):
    if request.method == 'POST':
        form = UsuarioEditForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('welcome')
    else:
        form = UsuarioEditForm(instance=request.user)

    return render(request, 'perfil.html', {'form': form})

#Actualizar Contrasena
@login_required
def cambiar_contrasena(request):
    if request.method == 'POST':
        form = CustomPasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Mantener al usuario autenticado después de cambiar la contraseña
            messages.success(request, '¡Tu contraseña ha sido cambiada exitosamente!')
            return redirect('welcome')  # Redirige a una página de perfil u otra página relevante
        else:
            messages.error(request, 'Por favor corrige los errores a continuación.')
    else:
        form = CustomPasswordChangeForm(user=request.user)

    return render(request, 'registration/cambiar_contrasena.html', {'form': form})