from django.db import models
from datetime import date
from apps.usuario.models import User
from apps.objeto.models import Service

# Create your models here.
class Exchange(model.Model):
	offeror = models.ForeignKey(User, on_delete = models.CASCADE)
	item_offered_by_offeror = models.ForeignKey(Service, on_delete = models.CASCADE)
	item_offered_by_receptor = models.ForeignKey(Service, on_delete = models.CASCADE)
	receiver = models.ForeignKey(User, on_delete = models.CASCADE)
	state = models.EmailField(max_lenght=254)
	donation_date = models.DateField(verbose_name= "Fecha de solicitud de intercambio", blank=False, null=False)
	acceptance_date = models.DateField(verbose_name= "Fecha de aceptación de intercambio", blank=False, null=False)


	"""docstring for Exchange"""
	def __init__(self, arg):
		super(Exchange, self).__init__()
		self.arg = arg
		