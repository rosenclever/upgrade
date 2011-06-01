from django.contrib import admin
from endereco.models import Endereco, Telefone

class EnderecoAdmin(admin.ModelAdmin):
	list_display = ('id','logradouro', 'numero', 'complemento', 'bairro', 'cidade', 'uf', 'cep')
	search_fields = ['logradouro', 'cep']
	list_filter = ['bairro']

class TelefoneAdmin(admin.ModelAdmin):
	list_display = ('id','tipo', 'numero', 'pessoa')
	search_fields = ['tipo', 'numero']
	list_filter = ['tipo']

admin.site.register(Telefone, TelefoneAdmin)
admin.site.register(Endereco, EnderecoAdmin)
