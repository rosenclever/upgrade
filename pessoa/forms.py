#-*- coding: utf-8 -*-
from django import forms
from pessoa.models import Pessoa
from endereco.models import Endereco, Telefone
from pessoa import validators

class PessoaForm(forms.ModelForm):
	class Meta:
		model = Pessoa
		exclude = ('endereco',)
#	SEXO = (
#		(u'M', u'Masculino'),
#		(u'F', u'Feminino')
#	)
	
#	TIPO_TELEFONE = (
#		(u'Res', u'Residencial'),
#		(u'Com', u'Comercial'),
#		(u'Cel', u'Celular'),
#		(u'Rad', u'Radio'),
#		(u'Rec', u'Recado')
#	)
	
#	nome = forms.CharField(max_length=100)
#	sexo = forms.ChoiceField(choices=SEXO)
#	dtNasc = forms.DateField(label=('Data de Nascimento'))
#	matricula = forms.CharField(max_length=5, required=False)
#	rg = forms.CharField(label=('RG'), max_length=15, required=False)
#	cpf = forms.CharField(label=('CPF'),max_length=11, min_length=11, required=False, validators=[validators.CpfValidator])
#	responsavel = forms.ChoiceField(required=False)
	
#	tipoTelefone = forms.ChoiceField(required=False,choices=TIPO_TELEFONE)
#	numeroTelefone = forms.CharField(required=False,max_length=11)
	
#	logradouro = forms.CharField(max_length=100)
#	numero = forms.IntegerField()
#	bairro = forms.CharField(max_length=50)
#	cidade = forms.CharField(max_length=50)
#	uf = forms.CharField(max_length=2)
#	cep = forms.IntegerField()
#	complemento = forms.CharField(max_length=100,required=False)
#	email = forms.EmailField(required=False)
	
#	def clean_cpf(self):
#		try:
#			pessoa = Pessoa.objects.get(cpf=self.cleaned_data['cpf'])
#		except Pessoa.DoesNotExist:
#			return self.cleaned_data['cpf']
#		raise forms.ValidationError(_(u'Este CPF já está inscrito.'))
	
#	def clean_rg(self):
#		try:
#			pessoa = Pessoa.objects.get(cpf=self.cleaned_data['rg'])
#		except Pessoa.DoesNotExist:
#			return self.cleaned_data['rg']
#		raise forms.ValidationError(_(u'Este rg já está inscrito.'))
		
#	def clean_email(self):
#		try:
#			pessoa = Pessoa.objects.get(cpf=self.cleaned_data['email'])
#		except Pessoa.DoesNotExist:
#			return self.cleaned_data['email']
#		raise forms.ValidationError(_(u'Este email já está inscrito.'))

	