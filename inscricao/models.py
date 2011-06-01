from django.db import models
from pessoa.models import Aluno
from cursos.models import Curso

class Inscricao(models.Model):
	aluno = models.ForeignKey(Aluno)
	curso = models.ForeignKey(Curso)
	totalParcelas = models.IntegerField()
	valorParcela = models.FloatField()
	diaVencimento = models.IntegerField()
	dataPrimeiraParcela = models.DateTimeField()
	desconto = models.FloatField()
	observacao = models.CharField(max_length=300)
	
	def __unicode__(self):
		return self.observacao

# Create your models here.
