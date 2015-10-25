# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registrasi', '0003_auto_20151024_2101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='registrasi',
            field=models.ForeignKey(to='registrasi.Registrasi'),
        ),
    ]
