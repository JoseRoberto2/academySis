# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-03 03:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gerenciador', '0003_auto_20170303_0252'),
    ]

    operations = [
        migrations.CreateModel(
            name='professores',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('nascimento', models.DateField()),
                ('cpf', models.CharField(max_length=14)),
                ('endereco', models.CharField(max_length=80)),
                ('numero', models.CharField(max_length=5)),
                ('complemento', models.CharField(blank=True, max_length=30)),
                ('bairro', models.CharField(max_length=40)),
                ('uf', models.CharField(choices=[('rn', 'Rio Grande do Norte'), ('pe', 'Pernabuco'), ('pb', 'Paraiba')], default='Rio Grande do Norte', max_length=2)),
                ('email', models.CharField(max_length=50)),
                ('telefone', models.CharField(max_length=13)),
            ],
        ),
        migrations.AlterField(
            model_name='aluno',
            name='uf',
            field=models.CharField(choices=[('rn', 'Rio Grande do Norte'), ('pe', 'Pernabuco'), ('pb', 'Paraiba')], default='Rio Grande do Norte', max_length=2),
        ),
    ]
