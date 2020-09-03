from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def Preguntas_Frecuentes(request):
    return render(request, "preguntas_frecuentes.html")

def Inicio(request):
    return render(request, "inicio2.html")