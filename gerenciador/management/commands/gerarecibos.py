from django.core.management.base import BaseCommand, CommandError
from gerenciador.models import *

class Command(BaseCommand):
    args = ''
    help = 'Export data to remote server'

    def handle(self, *args, **options):
        #d=despesa(referencia='domanage',valor='10',data_pagamento='2017-04-01',Pago=False)
        #d.save()
        al=turma_aluno.objects.all()
        for a in al:
            print a.pk
            r = recibo(turma_aluno=a, pago=False)
            r.save()


