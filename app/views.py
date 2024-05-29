from django.shortcuts import get_object_or_404, render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from app.models import Inmueble, Comuna, Region

# Create your views here.
def index(request):
    return render(request,'index.html', {})

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

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'

class CustomLogoutView(LogoutView):
    next_page = '/'