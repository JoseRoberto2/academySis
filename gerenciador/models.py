#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models


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

class turma(models.Model):
	nome = models.CharField(max_length=20)
	modalidade = models.CharField(max_length=13, choices=esporte)
	data_cadastro = models.DateTimeField(auto_now_add=True)
	valor = models.FloatField()
	dia_vencimento = models.CharField(max_length=2)