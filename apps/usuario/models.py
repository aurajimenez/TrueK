from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
	telefono = models.CharField(verbose_name="Teléfono", max_length=50)
	localizacion = models.CharField(verbose_name="Localización", max_length=100)
	photo = models.ImageField(upload_to ='Fotos_usuarios', null=True, blank=True)

	def __str__(self):
		return self.username

		