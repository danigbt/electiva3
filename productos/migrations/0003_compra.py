# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0002_producto_imagen'),
    ]

    operations = [
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('usuario', models.CharField(max_length=140)),
                ('email', models.EmailField(max_length=254)),
                ('tarjeta', models.CharField(max_length=16)),
                ('direccion', models.CharField(max_length=250, null=True)),
                ('telefono', models.CharField(max_length=40, null=True)),
                ('total', models.IntegerField(null=True)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('comfirmada', models.BooleanField(default=False)),
                ('producto', models.ManyToManyField(to='productos.Producto')),
            ],
            options={
                'verbose_name': 'Compra',
                'verbose_name_plural': 'Compras',
            },
        ),
    ]
