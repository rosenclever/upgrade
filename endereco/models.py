from django.db import models
from django.contrib import admin


class Endereco(models.Model):
	logradouro = models.CharField(max_length=100)
	numero = models.IntegerField()
	bairro = models.CharField(max_length=50)
	cidade = models.CharField(max_length=50)
	uf = models.CharField(max_length=2)
	cep = models.IntegerField()
	complemento = models.CharField(max_length=100,blank=True, null=True)
	email = models.EmailField(blank=True, null=True, unique=True)
	
	def __unicode__(self):
		return self.logradouro
		

class Telefone(models.Model):
	TIPO_TELEFONE = (
		(u'Res', u'Residencial'),
		(u'Com', u'Comercial'),
		(u'Cel', u'Celular'),
		(u'Rad', u'Radio'),
		(u'Rec', u'Recado')
	)
	tipo = models.CharField(max_length=3, choices=TIPO_TELEFONE)
	numero = models.CharField(max_length=11)
	from upgrade.pessoa.models import Pessoa
	pessoa = models.ForeignKey(Pessoa)
	
	def __unicode__(self):
		return self.numero


