from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.contrib.auth import logout
from .models import UsuarioN
from .models import UsuarioE
from .forms import UsuarioNForm
from django.http import JsonResponse

def home(request):
    context={}
    return render(request, 'generales/home.html')



@login_required
def store(request):
    context={}
    return render(request, 'generales/store.html')

def salir(request):
    context={}
    logout(request)
    return redirect('/')


from django.shortcuts import render, redirect
from .models import UsuarioN

def registrarUN(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        dpi = request.POST.get('dpi')
        fecha_nacimiento = request.POST.get('fecha_nacimiento')
        telefono = request.POST.get('telefono')
        nombre_usuario = request.POST.get('nombre_usuario')
        correo_electronico = request.POST.get('correo_electronico')
        contraseña = request.POST.get('contraseña')
        confirmacion_contraseña = request.POST.get('confirmacion_contraseña')
        
        # Guardar los datos en la base de datos
        usuario = UsuarioN(nombre=nombre, apellido=apellido, dpi=dpi, fecha_nacimiento=fecha_nacimiento,
                           telefono=telefono, nombre_usuario=nombre_usuario, correo_electronico=correo_electronico,
                           contraseña=contraseña, confirmacion_contraseña=confirmacion_contraseña)
        usuario.save()
        
        # Redirigir a alguna página de confirmación o a donde desees
        return redirect('/')  # Reemplaza 'confirmacion_registro' con el nombre de la URL de confirmación
        
    return render(request, 'registration/login.html')  # Reemplaza 'tu_template.html' con el nombre de tu plantilla donde está el formulario


def registrarUE(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        dpi = request.POST.get('dpi')
        usuario = request.POST.get('usuario')
        contraseña = request.POST.get('contraseña')
        confirmacion_contraseña = request.POST.get('confirmacion_contraseña')
        
        # Guardar los datos en la base de datos
        usuario = UsuarioE(nombre=nombre, apellido=apellido, dpi=dpi, usuario=usuario,
                           contraseña=contraseña, confirmacion_contraseña=confirmacion_contraseña)
        usuario.save()
        
        # Redirigir a alguna página de confirmación o a donde desees
        return redirect('listadoE')  # Reemplaza 'confirmacion_registro' con el nombre de la URL de confirmación
        
    return render(request, 'registration/signupe.html')  # Reemplaza 'tu_template.html' con el nombre de tu plantilla donde está el formulario





def listadoN(request):
    usuarios = UsuarioN.objects.all()
    return render(request, 'generales/listadoN.html', {'usuarios': usuarios})

def listadoE(request):
    usuariose = UsuarioE.objects.all()
    return render(request, 'generales/listadoE.html', {'usuariose': usuariose})


def eliminarN(request, id):
    user=UsuarioN.objects.get(id=id)
    user.delete()
    return redirect('/')

def signupn(request):
    context={}
    return render(request, 'registration/signupn.html')

def signupe(request):
    context={}
    return render(request, 'registration/signupe.html')


def login_view(request):
    return render(request, 'generales/login_view.html')

def logout_view(request):
    logout(request)
    return render('/')

@login_required
def home_view(request):
    return render(request, 'generales/home_view.html')

def find_user_view(request):
    #si es capaz de encontrar al usuario
    return JsonResponse({'success': True})