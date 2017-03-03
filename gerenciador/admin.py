from django.contrib import admin

# Register your models here.
from gerenciador.models import *

class alunoAdmin(admin.ModelAdmin):
	list_display = ('nome','data_cadastro')
	search_fields = ('nome','cpf')

class anotacoesAdmin(admin.ModelAdmin):
	list_display = ('aluno','data_cadastro','anotacao')

class despesaAdmin(admin.ModelAdmin):
	list_display = ('referencia', 'valor','Pago')

admin.site.register(aluno, alunoAdmin)
admin.site.register(professor)
admin.site.register(turma)
admin.site.register(despesa, despesaAdmin)
admin.site.register(anotacoes_aluno, anotacoesAdmin)
admin.site.register(turma_aluno)