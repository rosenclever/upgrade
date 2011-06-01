from django.contrib import admin
from cursos.models import Curso
from turmas.models import Turma

class TurmaInline(admin.TabularInline):
	model = Turma
	extra = 1
	
class CursoAdmin(admin.ModelAdmin):
	list_display = ('id','nome', 'cargaHoraria', 'valorTotal')
	search_fields = ['nome', 'cargaHoraria']
	list_filter = ['cargaHoraria']
	inlines = [TurmaInline]


admin.site.register(Curso, CursoAdmin)
#admin.site.register(Endereco, EnderecoAdmin)
