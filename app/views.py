from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from app.models import Inmueble, Comuna, Region
from .forms import CustomUserCreationForm, InmuebleForm

# Create your views here.
def index(request):
    return render(request,'index.html', {})

#detall del inmueble
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
            user = authenticate(username=user_creation_form.cleaned_data['username'], password=user_creation_form.cleaned_data['password1'])
            login(request, user)
            return redirect('indice')
        else:
            data['form'] = user_creation_form

    return render(request, 'registration/register.html', data)


#login
class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
class CustomLogoutView(LogoutView):
    next_page = '/'


#Muestra inmuebles segun logeo
@login_required
def welcome(request):
    inmuebles = Inmueble.objects.all()
    comunas = Comuna.objects.all()
    regiones = Region.objects.all()
    return render(request, 'welcome.html', {
        'inmuebles':  inmuebles, 
        'comunas': comunas,
        'regiones': regiones,
        })

#Crear Inmueble
@login_required
def crear_inmueble(request):
    if request.method == 'POST':
        form = InmuebleForm(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            inmueble = form.save(commit=False)
            inmueble.propietario = request.user.usuario
            inmueble.save()
            return redirect('dashboard') 
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
            return redirect('dashboard',pk=inmueble.id)
    else:
        form = InmuebleForm(instance=inmueble)
    return render(request, 'registration/actualizar_inmueble.html', {'form': form})

#Eliminar Inmueble
@login_required
def eliminar_inmueble(request, id):
    inmueble = get_object_or_404(Inmueble, pk=id)
    if request.method == 'POST':
        inmueble.delete()
        return redirect('dashboard')
    else:
        return render(request,'registration/eliminar_inmueble.html', {'inmueble':inmueble} )



