#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from django_cron import CronJobBase, Schedule


# Create your models here.
estados=(
	('rn','Rio Grande do Norte'),
	('pe','Pernabuco'),
	('pb','Paraiba'),
	)
esporte=(
	('boxe', 'Boxe'),
	('capoeira','Capoeira'),
	('judo',u"Judô"),
	('taekwond','Taekwond'),
	('mma','MMA'),
	('jiujitsu','Jiu Jitsu'),
	('karate',u'Karatê'),
	('zumba','Zumba'),
	('outra','Outra')
	)

class aluno(models.Model):
	nome = models.CharField(max_length=100)
	data_nasc = models.DateField()
	cpf = models.CharField(max_length=14)
	email = models.EmailField()
	endereco = models.CharField(max_length=80)
	numero = models.CharField(max_length=5)
	complemento = models.CharField(max_length=30, blank=True)
	bairro = models.CharField(max_length=40)
	uf = models.CharField(max_length=2, choices=estados, default='Rio Grande do Norte')
	telefone = models.CharField(max_length=13)
	data_cadastro = models.DateTimeField(auto_now_add=True)
	pass
	def __unicode__(self):
		return self.nome

class professor(models.Model):
	nome = models.CharField(max_length=100)
	nascimento = models.DateField()
	cpf = models.CharField(max_length=14)
	endereco = models.CharField(max_length=80)
	numero = models.CharField(max_length=5)
	complemento = models.CharField(max_length=30, blank=True)
	bairro = models.CharField(max_length=40)
	uf = models.CharField(max_length=2, choices=estados, default='Rio Grande do Norte')
	email = models.EmailField()
	telefone = models.CharField(max_length=13)
	def __unicode__(self):
		return self.nome

class turma(models.Model):
	nome = models.CharField(max_length=20)
	modalidade = models.CharField(max_length=13, choices=esporte)
	data_cadastro = models.DateTimeField(auto_now_add=True)
	valor = models.DecimalField(max_digits=8, decimal_places=2)
	dia_vencimento = models.CharField(max_length=2)
	professor = models.ForeignKey(professor, on_delete=models.CASCADE)
	turma_alunos = models.ManyToManyField(aluno, through='turma_aluno')
	def __unicode__(self):
		return '%s - %s' % (self.nome,self.modalidade)

class despesa(models.Model):
	referencia = models.CharField(max_length=30)
	valor = models.DecimalField(max_digits=8, decimal_places=2)
	data_pagamento = models.DateField()
	Pago = models.BooleanField()
	def statusDs(self):
		return self.Pago
	

class anotacoes_aluno(models.Model):
	data_cadastro = models.DateTimeField(auto_now_add=True)
	anotacao = models.TextField()
	aluno = models.ForeignKey(aluno, on_delete=models.CASCADE)

class turma_aluno(models.Model):
	alunos = models.ForeignKey(aluno, on_delete=models.CASCADE)
	turma = models.ForeignKey(turma, on_delete=models.CASCADE)
	data_matricula = models.DateField(auto_now_add=True)

class MyCronJob(CronJobBase):
	RUN_EVERY_MINS = 2
	#schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
	RUN_AT_TIMES = ['15:02']
	schedule = Schedule(run_every_mins=RUN_EVERY_MINS, run_at_times=RUN_AT_TIMES)
	code = 'gerenciador.my_cron_job'  # a unique code
	def do(self):
		print 'funconado cron'
		b=despesa(referencia='teste',valor='10',data_pagamento='2017-04-01',Pago=False)
		b.save()
		pass
	# do your thing here