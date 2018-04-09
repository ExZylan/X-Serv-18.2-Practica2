from django.db import models

# Create your models here.

class Url(models.Model):
	Direccion = models.CharField(max_length=128)
	def __str__(self):
			return self.Direccion