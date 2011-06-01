from django.contrib import admin
from pessoa.models import Aluno
from cursos.models import Curso
from inscricao.models import Inscricao



class InscricaoAdmin(admin.ModelAdmin):
	list_display = ('id', 'totalParcelas', 'valorParcela', 'diaVencimento', 'dataPrimeiraParcela', 'desconto','observacao')
	search_fields = ['dataVencimento', 'diaVencimento']
	list_filter = ['diaVencimento']
	#inlines = [AlunoInline, CursoInline]


admin.site.register(Inscricao, InscricaoAdmin)