from django.db import models

# Create your models here.
class Fir(models.Model):
	name = models.CharField(max_length=128)
	address = models.CharField(max_length=500)
	complaint = models.CharField(max_length=1500)

	def __str__(self):
		return f"{self.name} {self.address} {self.complaint}"