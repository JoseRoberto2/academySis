# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-06 23:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gerenciador', '0012_recibo_pago'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recibo',
            name='forma_pagamento',
            field=models.CharField(blank=True, choices=[('dinheiro', 'Dinheiro(R$)'), ('Cart\xe3o', 'Cart\xe3o'), ('Tranferencia', 'Tranfer\xeancia')], max_length=20),
        ),
    ]
