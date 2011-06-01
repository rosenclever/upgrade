from django import forms
from endereco.models import Endereco, Telefone

class EnderecoForm(forms.ModelForm):
	class Meta:
		model = Endereco

class TelefoneForm(forms.ModelForm):
	class Meta:
		model = Telefone
		exclude = ('pessoa',)
