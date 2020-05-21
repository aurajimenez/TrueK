from django.db import models

from datetime import date

from apps.usuario.models import Usuario
from apps.producto.models import Producto

class Intercambio(models.Model):

	ESTADOS = (
		('Iniciado','Iniciado'),
		('Aceptado','Aceptado'),
		('Rechazado','Rechazado'),
	)

	oferente = models.ForeignKey(Usuario, related_name="oferente", on_delete = models.CASCADE)
	producto_del_oferente = models.ForeignKey(Producto, related_name="productos_del_oferente", on_delete = models.CASCADE)
	producto_del_receptor = models.ForeignKey(Producto, related_name="productos_del_receptor", on_delete = models.CASCADE)
	receptor = models.ForeignKey(Usuario, related_name="receptor", on_delete = models.CASCADE)
	estado = models.CharField(max_length=254, choices = ESTADOS)
	fecha_solicitud_intercambio = models.DateField(verbose_name= "Fecha de solicitud de intercambio", blank=False, default= date.today())
	fecha_aceptacion_intercambio = models.DateField(verbose_name= "Fecha de aceptación de intercambio", blank=True, null=True)
