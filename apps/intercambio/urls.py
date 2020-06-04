from django.urls import path

from . import views

app_name = 'intercambio'
urlpatterns = [

	path('registrar_desde_producto/<int:producto_id>', views.RegistrarDesdeProducto, name="registrar_desde_producto"),
	path('registrar', views.Registrar, name="registrar"),
    path('modificar/<int:intercambio_id>', views.Modificar, name='modificar'),
	path('listar', views.Listar, name="listar"),
	path('aceptar/<int:intercambio_id>', views.Aceptar, name='aceptar'),
	path('rechazar/<int:intercambio_id>', views.Rechazar, name='rechazar'),
	path('cancelar/<int:intercambio_id>', views.Cancelar, name='cancelar'),
    path('perfil/<int:intercambio_id>', views.Perfil, name='perfil'),
]