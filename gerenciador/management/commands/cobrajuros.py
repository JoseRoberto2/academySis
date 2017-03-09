from django.core.management.base import BaseCommand, CommandError
from gerenciador.models import *
from datetime import date

class Command(BaseCommand):
    args = ''
    help = 'Export data to remote server'

    def handle(self, *args, **options):
        al=recibo.objects.all()
        for a in al:
            #print a.pk
            if(a.pago==False):
                dia_hj=float(date.today().day)
                dia_vc=float(a.turma_aluno.dia_vencimento)

                if(dia_hj>dia_vc):
                    a.juros = float(a.valor()) * 0.1 * (dia_hj - dia_vc)
                    a.save()