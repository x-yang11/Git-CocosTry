# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='inoutdbview',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('date', models.CharField(max_length=8)),
                ('type', models.CharField(max_length=128)),
                ('money_type', models.CharField(max_length=128)),
                ('category', models.CharField(max_length=128)),
                ('amount', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
