from django.contrib import admin

# Register your models here.
from gerenciador.models import *

admin.site.register(aluno)
admin.site.register(professor)
admin.site.register(turma)