from django.db import models
from datetime import date
from apps.usuario.models import User
from apps.objeto.models import Service


# Create your models here.
class Donation(models.Model):
	donor = models.ForeignKey(User, on_delete = models.CASCADE)
	objects = models.ForeignKey(Service, on_delete = models.CASCADE)
	receiver = models.CharField(User, on_delete = models.CASCADE)
	state = models.CharField(max_lenght=254)
	donation_date = models.DateField(verbose_name= "Fecha de donación", blank=False, null=False)
	receipt_date = models.DateField(verbose_name= "Fecha de aceptación", blank=False, null=False)


	"""docstring for Donation"""
	def __init__(self, arg):
		super(Donation, self).__init__()
		self.arg = arg
		