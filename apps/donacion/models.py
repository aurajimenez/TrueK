from django.db import models

# Create your models here.
class Donation(models.Model):
	donor = models.ForeignKey(User, on_delete = models.CASCADE)
	objects = models.ForeignKey(Service, on_delete = models.CASCADE)
	receiver = models.CharField(User, on_delete = models.CASCADE)
	state = models.EmailField(max_lenght=254)
	donation_date = models.DateField()
	receipt_date = models.DateField()


	"""docstring for Donation"""
	def __init__(self, arg):
		super(Donation, self).__init__()
		self.arg = arg
		