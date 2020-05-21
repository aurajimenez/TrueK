from django.db import models
from django.utils import timezone

from datetime import date, datetime

from apps.usuario.models import Usuario
from apps.producto.models import Producto

class Donacion(models.Model):

	ESTADOS = (
		('Iniciada','Iniciada'),
		('Recibida','Recibida'),
		('Rechazada','Rechazada'),
	)

	donador = models.ForeignKey(Usuario, related_name="donaciones_realizadas", on_delete=models.CASCADE)
	objecto_servicio = models.ForeignKey(Producto, on_delete = models.CASCADE)
	receptor = models.ForeignKey(Usuario, related_name="donaciones_recibidas", on_delete=models.CASCADE)
	estado = models.CharField(max_length=70, choices=ESTADOS)
	fecha_donacion = models.DateTimeField(verbose_name="Fecha de donación", default=timezone.now)
	fecha_aceptacion = models.DateField(verbose_name="Fecha de aceptación", blank=True, null=True)
