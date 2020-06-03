from django.urls import path

from . import views

app_name = 'producto'
urlpatterns = [
     path('registrar', views.Registrar, name='registrar'),
     path('modificar/<int:producto_id>', views.Modificar, name='modificar'),
     path('listar', views.Listar, name='listar'),
     path('perfil/<int:producto_id>', views.Perfil, name='perfil'),

]