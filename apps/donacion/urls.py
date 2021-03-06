from django.urls import path

from . import views

app_name = 'donacion'
urlpatterns = [

	path('registrar_desde_producto/<int:producto_id>', views.RegistrarDesdeProducto, name="registrar_desde_producto"),
	path('registrar', views.Registrar, name="registrar"),
    path('modificar/<int:donacion_id>', views.Modificar, name='modificar'),
	path('listar', views.Listar, name="listar"),
	path('aceptar/<int:donacion_id>', views.Aceptar, name='aceptar'),
	path('rechazar/<int:donacion_id>', views.Rechazar, name='rechazar'),
	path('cancelar/<int:donacion_id>', views.Cancelar, name='cancelar'),
    path('perfil/<int:donacion_id>', views.Perfil, name='perfil'),
]