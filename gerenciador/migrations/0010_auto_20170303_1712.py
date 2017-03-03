# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-03 17:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gerenciador', '0009_anotacoes_aluno'),
    ]

    operations = [
        migrations.CreateModel(
            name='turma_aluno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_matricula', models.DateField(auto_now_add=True)),
                ('alunos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gerenciador.aluno')),
            ],
        ),
        migrations.AddField(
            model_name='turma',
            name='professor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='gerenciador.professor'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='turma_aluno',
            name='turma',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gerenciador.turma'),
        ),
        migrations.AddField(
            model_name='turma',
            name='turma_alunos',
            field=models.ManyToManyField(through='gerenciador.turma_aluno', to='gerenciador.aluno'),
        ),
    ]