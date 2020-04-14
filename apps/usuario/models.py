from django.db import models

# Create your models here.
class User(models.Model):
	name = models.CharField(verbose_name="Nombre", max_lenght=100)
	phone = models.CharField(verbose_name="Teléfono", max_lenght=50)
	localizacion = models.CharField(verbose_name="Localización", max_lenght=100)
	email = models.EmailField(max_lenght=254)
	photo = models.ImageField()


	"""docstring for User"""
	def __init__(self, arg):
		super(User, self).__init__()
		self.arg = arg
		