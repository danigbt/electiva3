# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0003_compra'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compra',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='compra',
            name='tarjeta',
            field=models.CharField(max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name='compra',
            name='usuario',
            field=models.CharField(max_length=140, null=True),
        ),
    ]
