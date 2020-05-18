from django.urls import path

from . import views

app_name = 'donacion'
urlpatterns = [

	path('registrar', views.Registrar, name="registrar"),
    path('modificar/<int:donacion_id>', views.Modificar, name='modificar'),
	path('listar', views.Listar, name="listar"),

]