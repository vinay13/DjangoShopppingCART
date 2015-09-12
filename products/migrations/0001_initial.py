# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('description', models.SlugField(max_length=150)),
                ('photo', models.ImageField(blank=True, upload_to='product_photo')),
                ('manufacturer', models.CharField(blank=True, max_length=300)),
                ('price_in_dollars', models.DecimalField(max_digits=6, decimal_places=2)),
                ('slug', models.SlugField(max_length=300)),
            ],
        ),
    ]
