from django.urls import path

from . import views

app_name = 'producto'
urlpatterns = [
     path('registrar', views.Registrar, name='registrar'),
     path('listar', views.Listar, name='listar'),
]