# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DailyDo',
            fields=[
                ('date_info_date', models.DateField(serialize=False, primary_key=True)),
                ('gratitude1_text', models.CharField(max_length=500, blank=True)),
                ('gratitude2_text', models.CharField(max_length=500, blank=True)),
                ('gratitude3_text', models.CharField(max_length=500, blank=True)),
                ('positive_exp_text', models.CharField(max_length=500, blank=True)),
                ('exercise_bool', models.BooleanField(default=False)),
                ('meditation_bool', models.BooleanField(default=False)),
                ('kind_act_text', models.CharField(max_length=500, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PwdInfo',
            fields=[
                ('pwd_purpose_text', models.CharField(max_length=50, serialize=False, primary_key=True, blank=True)),
                ('pwd_text', models.CharField(max_length=500, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
