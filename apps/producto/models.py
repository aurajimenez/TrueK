from django.db import models

from apps.usuario.models import Usuario

class Producto(models.Model):

	ESTADOS = (
		('Vigente','Vigente'),
		('Donado','Donado'),
		('Aceptado','Aceptado'),
		('Rechazado','Rechazado'),
	)

	dueno = models.ForeignKey(Usuario, on_delete = models.CASCADE)
	nombre = models.CharField(verbose_name="Nombre", max_length=100)
	descripcion = models.TextField()
	foto = models.ImageField(upload_to ='media', null=True, blank=True)
	etiquetas = models.CharField(verbose_name="Tags", max_length=100)
	estado = models.CharField(verbose_name="Estado", max_length=100, choices=ESTADOS)

	def __str__(self):
		return self.nombre

