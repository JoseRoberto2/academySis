from django.core.management.base import BaseCommand, CommandError
#from gerenciador.models import despesa

class Command(BaseCommand):
    args = ''
    help = 'Export data to remote server'

    def handle(self, *args, **options):
        p=open('/home/roberto/Documentos/testandoaa.txt', 'r+')
        p.writelines('acessando arquivo')
        p.close()
