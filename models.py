from django.db import models

class PredResults(models.Model):

	age = models.FloatField()
	workclass = models.CharField(max_length=100)
	education_years = models.FloatField()
	marital_status = models.CharField(max_length=100)
	relationship = models.CharField(max_length=100)
	race = models.CharField(max_length=100)
	sex = models.CharField(max_length=100)
	hours_per_week = models.FloatField()
	result = models.CharField(max_length=30)

	def __str__(self):
		return self.result



