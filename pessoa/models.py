from django.db import models
from django.contrib import admin
from upgrade.endereco.models import Endereco

class Pessoa(models.Model):
	TIPO_SEXO = (
		(u'M', u'Masculino'),
		(u'F', u'Feminino')
	)
	nome = models.CharField("Nome", max_length=100)
	sexo = models.CharField("Sexo",max_length=1, choices=TIPO_SEXO)
	dt_nasc = models.DateField("Data de Nascimento")
	matricula = models.CharField("Matricula", max_length=5, null=True, blank=True, unique=True)
	rg = models.CharField("RG", max_length=15, null=True, blank=True, unique=True)
	cpf = models.CharField("CPF", max_length=11, null=True, blank=True, unique=True)
	endereco = models.ForeignKey(Endereco, verbose_name="endereco")
	responsavel = models.ForeignKey('self', verbose_name="responsavel")
	
	def __unicode__(self):
		return self.nome
