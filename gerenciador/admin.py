from django.contrib import admin

# Register your models here.
from gerenciador.models import *

class alunoAdmin(admin.ModelAdmin):
	list_display = ('nome','data_cadastro','imagem_img')
	search_fields = ('nome','cpf')

class anotacoesAdmin(admin.ModelAdmin):
	list_display = ('aluno','data_cadastro','anotacao')

class despesaAdmin(admin.ModelAdmin):
	list_display = ('referencia', 'valor','Pago')

class professorAdmin(admin.ModelAdmin):
	list_display = ('nome', 'telefone','endereco','numero','bairro')
	search_fields = ('nome', 'bairro', 'endereco')

class turmaAdmin(admin.ModelAdmin):
	list_display = ('nome', 'modalidade','valor','professor')

class turma_alunoAdmin(admin.ModelAdmin):
	list_display = ('turma','alunos','dia_vencimento','data_matricula')

	#search_fields = ('turma', 'alunos')

class recibosAdmin(admin.ModelAdmin):
	list_display = ('turma_aluno','forma_pagamento','valor','juros','total','vencimento','mes','pago')
	#search_fields = ('')

admin.site.register(aluno, alunoAdmin)
admin.site.register(professor, professorAdmin)
admin.site.register(turma, turmaAdmin)
admin.site.register(despesa, despesaAdmin)
admin.site.register(anotacoes_aluno, anotacoesAdmin)
admin.site.register(turma_aluno, turma_alunoAdmin)
admin.site.register(recibo,recibosAdmin)