# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-02 01:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitorias', '0007_seccionmonitoria_payment_method'),
    ]

    operations = [
        migrations.AddField(
            model_name='seccionmonitoria',
            name='seccion_payed',
            field=models.BooleanField(default=False),
        ),
    ]