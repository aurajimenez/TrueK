from django.db import models

class Usuario(models.Model):
	nombre = models.CharField(verbose_name="Nombre", max_length=100)
	telefono = models.CharField(verbose_name="Teléfono", max_length=50)
	localizacion = models.CharField(verbose_name="Localización", max_length=100)
	email = models.EmailField(max_length=254)
	photo = models.ImageField()

	def __str__(self):
		return self.nombre

		