from django.db import models
from cursos.models import Curso

class Turma(models.Model):
	sigla = models.CharField(max_length=10)
	previsaoInicio = models.DateTimeField()
	previsaoTermino = models.DateTimeField()
	turma = models.ForeignKey(Curso)

	
	def __unicode__(self):
		return self.sigla


# Create your models here.
