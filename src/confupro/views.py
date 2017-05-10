from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


def inicio(request):
    #html = "<html><body>Hola Mundo</body></html>"
    #return HttpResponse(html)
    return render(request, 'inicio.html')

def usuario_nuevo(request):
    if request.method=='POST':
        formulario = UserCreationForm(request.POST)
        if formulario.is_valid:
            print (formulario)
            formulario.save()
            return HttpResponseRedirect('/')
    else:
        formulario = UserCreationForm()
    context = {'formulario': formulario}
    return render(request, 'usuario_nuevo.html', context)

def usuario_login(request):
    if not request.user.is_anonymous():
        return HttpResponseRedirect('/usuario/perfil')
    if request.method == 'POST':
        formulario = AuthenticationForm(request.POST)
        if formulario.is_valid:
            usuario = request.POST['username']
            clave = request.POST['password']
            acceso = authenticate(username=usuario, password=clave)
            if acceso is not None:
                if acceso.is_active:
                    login(request, acceso)
                    return HttpResponseRedirect('/usuario/perfil')
                else:
                    return render(request, 'error_usuario_noactivo.html')
            else:
                return render(request, 'error_usuario_nousuario.html')
    else:
        formulario = AuthenticationForm()
    context = {'formulario': formulario}
    return render(request, 'login.html', context)

@login_required(login_url='/usuario/login/')
def usuario_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

@login_required(login_url='/usuario/login/')
def usuario_perfil(request):
	usuario = request.user
	context = {'usuario': usuario}
	return render(request, 'usuario_perfil.html', context)





