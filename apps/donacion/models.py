from django.db import models

from datetime import date

from apps.usuario.models import Usuario
from apps.producto.models import Producto

class Donacion(models.Model):

	ESTADOS = (
		('Vigente','Vigente'),
		('No Vigente','No Vigente'),
		('Recibida','Recibida'),
		('Rechazada','Rechazada'),
	)

	donador = models.ForeignKey(Usuario, related_name="donaciones_realizadas", on_delete=models.CASCADE)
	objecto_servicio = models.ForeignKey(Producto, on_delete = models.CASCADE)
	receptor = models.ForeignKey(Usuario, related_name="donaciones_recibidas", on_delete=models.CASCADE)
	estado = models.CharField(max_length=254, choices=ESTADOS)
	fecha_donacion = models.DateField(verbose_name="Fecha de donación", blank=True, null=True)
	fecha_aceptacion = models.DateField(verbose_name="Fecha de aceptación", blank=True, null=True)
