from django.db import models

# Create your models here.
class Url(models.Model):
	original = models.CharField(max_length=2083)
	short = models.CharField(max_length=500)

	def __str__(self):
		urls = self.original + self.short
		return urls