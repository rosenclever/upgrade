from django.contrib import admin
from pessoa.models import Pessoa
from endereco.models import Telefone, Endereco

class TelefoneInline(admin.TabularInline):
	model = Telefone
	extra = 1

class EnderecoInline(admin.TabularInline):
	model = Endereco
	extra = 1



class PessoaAdmin(admin.ModelAdmin):
	list_display = ('id', 'matricula', 'nome', 'sexo', 'dt_nasc', 'rg', 'cpf', 'responsavel')
	search_fields = ['matricula', 'nome', 'dt_nasc']
	list_filter = ['sexo']
	inlines = [EnderecoInline]
	inlines = [TelefoneInline]

admin.site.register(Pessoa, PessoaAdmin)