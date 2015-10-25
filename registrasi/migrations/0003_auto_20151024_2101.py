# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registrasi', '0002_auto_20151023_0214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='nomor_member',
            field=models.CharField(max_length=12, serialize=False, primary_key=True),
        ),
    ]
