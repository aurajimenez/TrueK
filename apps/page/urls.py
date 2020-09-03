from django.urls import path

from . import views

app_name = 'pages'
urlpatterns = [

    path('inicio', views.Inicio, name='inicio'),	
    path('preguntas_frecuentes', views.Preguntas_Frecuentes, name='preguntas_frecuentes'),

]