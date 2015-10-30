# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('emp_id', models.IntegerField()),
                ('email_id', models.EmailField(max_length=254)),
                ('emp_deg', models.CharField(max_length=50)),
                ('department_name', models.CharField(max_length=50)),
                ('reporting_name', models.CharField(max_length=50)),
                ('seating_location', models.CharField(max_length=50)),
                ('mobile_no', models.CharField(max_length=12)),
                ('extn_no', models.CharField(default=b'', max_length=12)),
            ],
        ),
    ]
