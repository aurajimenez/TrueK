from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
	telefono = models.CharField(verbose_name="Teléfono", max_length=50)
	localizacion = models.CharField(verbose_name="Localización", max_length=100)
	photo = models.ImageField(upload_to ='Fotos_usuarios', null=True, blank=True, default='th2.png')

	@staticmethod
	def crear_usuario_inicial():
		total_usuarios = Usuario.objects.all().count()
		if total_usuarios == 0:
			password = "historias"
			user = Usuario.objects.create_user('admin1', 'root@gmail.com', password)
			user.set_password(password)
			user.first_name = 'Administrador'
			user.is_superuser = True
			user.is_staff = True
			user.save()

	def __str__(self):
		return self.username

		