from django.urls import path

from . import views

app_name = 'usuario'
urlpatterns = [
	
	path('registrar', views.Registrar, name="registrar"),
	path('registrarme', views.RegistrarMe, name="registrarme"),
    path('modificar/<int:usuario_id>', views.Modificar, name='modificar'),
	path('listar', views.Listar, name="listar"),
	path('login', views.Login, name="login"),
	path('logout', views.Logout, name="logout"),
    path('inicio', views.Inicio, name='inicio'),
    path('perfil/<int:usuario_id>', views.Perfil, name='perfil'),
    path('cambiar_contrasena/<int:usuario_id>', views.Cambiar_contrasena, name='cambiar_contrasena'),

]