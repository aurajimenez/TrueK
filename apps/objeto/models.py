from django.db import models
from apps.usuario.models import User

# Create your models here.
class Service(models.Model):
	owner = models.ForeignKey(User, on_delete = models.CASCADE)
	name = models.CharField(verbose_name="Nombre", max_lenght=100)
	description = models.TextField()
	photo = models.ImageField()
	tags = models.CharField(verbose_name="Nombre", max_lenght=100)
	state = models.CharField(verbose_name="Nombre", max_lenght=100)

	"""docstring for Service"""
	def __init__(self, arg):
		super(Service, self).__init__()
		self.arg = arg
		