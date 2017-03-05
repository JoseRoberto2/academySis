from django_cron import CronJobBase, Schedule
from gerenciador.models import *


class MyCronJob(CronJobBase):
    RUN_EVERY_MINS = 2
    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'gerenciador.my_cron_job'  # a unique code
    def do(self):
        print 'funconado cron'
        b=despesa(referencia='teste',valor='10',data_pagamento='2017-04-01',Pago=False)
        b.save()
        pass
    # do your thing here