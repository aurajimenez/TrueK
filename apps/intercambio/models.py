from django.db import models

# Create your models here.
class Exchange(model.Model):
	offeror = models.ForeignKey(User, on_delete = models.CASCADE)
	item_offered_by_offeror = models.ForeignKey(Service, on_delete = models.CASCADE)
	item_offered_by_receptor = models.ForeignKey(Service, on_delete = models.CASCADE)
	receiver = models.ForeignKey(User, on_delete = models.CASCADE)
	state = models.EmailField(max_lenght=254)
	donation_date = models.DateField()
	acceptance_date = models.DateField()


	"""docstring for Exchange"""
	def __init__(self, arg):
		super(Exchange, self).__init__()
		self.arg = arg
		