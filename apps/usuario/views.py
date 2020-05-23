from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Usuario
from .forms import RegistrarUsuarioForm, ModificarUsuarioForm

@login_required
def Registrar(request):
    if request.method == 'POST':
        form = RegistrarUsuarioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('usuario:listar')
    else:
        form = RegistrarUsuarioForm()
    return render(request, "registrar_usuario.html", {'form': form})

@login_required
def Modificar(request, usuario_id):
    usuario = Usuario.objects.get(id=usuario_id)
    form = ModificarUsuarioForm(instance=usuario)
    if request.method == "POST":
        form = ModificarUsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            usuario = form.save(commit=False)
            form.save()
            return redirect('usuario:listar')
    return render(request, 'modificar_usuario.html',{'form': form})

@login_required
def Listar(request):
    usuarios = Usuario.objects.all()
    return render(request, "listar_usuarios.html", {'usuarios':usuarios})


def Login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # los campos username y password son los que utiliza el form: "AuthenticationForm"
            # en mi caso accedí como el usuario que acabo de crear
            # cono
            # cono
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username} ")
                return redirect('usuario:listar')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, "login.html", {'form': form})

@login_required
def Logout(request):
    logout(request)
    return redirect("login.html")