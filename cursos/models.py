from django.db import models

class Curso(models.Model):
	nome = models.CharField(max_length=50)
	cargaHoraria = models.IntegerField()
	valorTotal = models.FloatField()
	
	def __unicode__(self):
		return self.nome


# Create your models here.
