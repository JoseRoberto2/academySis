#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
#from django_cron import CronJobBase, Schedule


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
pagamentos=(
	('dinheiro', 'Dinheiro(R$)'),
	('Cartão', 'Cartão'),
	('Tranferencia', 'Tranferência'),
)
meses= {
	('1', 'JANEIRO'),
	('2', 'FEVEREIRO'),
	('3', 'MARÇO'),
	('4', 'ABRIL'),
	('5', 'MAIO'),
	('6', 'JUNHO'),
	('7', 'JULHO'),
	('8', 'AGOSTO'),
	('9', 'SETEMBRRO'),
	('10', 'OUTUBRO'),
	('11', 'NOVEMBRO'),
	('12', 'DEZEMBRO'),
}

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
	foto_perfil = models.ImageField(blank=True)
	pass

	def __unicode__(self):
		return self.nome

	def imagem_img(self):
		if self.foto_perfil:
			return u'<img src="%s" width=50 />' % self.foto_perfil.url
		else:
			return u'Sem imagem'
	imagem_img.short_description = "Imagem Perfil"
	imagem_img.allow_tags = True

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
	#dia_vencimento = models.CharField(max_length=2)
	professor = models.ForeignKey(professor, on_delete=models.CASCADE)
	turma_alunos = models.ManyToManyField(aluno, through='turma_aluno')
	def __unicode__(self):
		return '%s - %s' % (self.nome,self.modalidade)

	def rtValor(self):
		return self.valor

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
	dia_vencimento = models.CharField(max_length=2, default='02')
	def __unicode__(self):
		return ('%s %s' % (unicode(self.turma), unicode(self.alunos)))
		#return unicode(self.turma.nome)


class recibo(models.Model):
	turma_aluno=models.ForeignKey(turma_aluno, on_delete=models.CASCADE)
	forma_pagamento=models.CharField(max_length=20, choices=pagamentos, blank=True)
	observacao=models.TextField(blank=True)
	pago = models.BooleanField()
	mes = models.CharField(max_length=2,choices=meses)
	juros = models.DecimalField(max_digits=8, decimal_places=2, default=0, blank=True,editable=False)
	#def __unicode__(self):
		#return self.turma_aluno.turma.valor

	def valor(self):
		return self.turma_aluno.turma.valor

	def vencimento(self):
		return self.turma_aluno.dia_vencimento

	def total(self):
		return self.valor()+self.juros