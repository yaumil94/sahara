# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registrasi', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='registrasi',
            options={'verbose_name_plural': 'Data Calon Member (Registrasi)', 'verbose_name': 'Calon Member'},
        ),
        migrations.AddField(
            model_name='registrasi',
            name='jenis_kelamin',
            field=models.CharField(max_length=1, default='P', choices=[('P', 'Pria'), ('W', 'Wanita')]),
        ),
        migrations.AlterField(
            model_name='registrasi',
            name='nomer_registrasi',
            field=models.CharField(unique=True, max_length=10, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='registrasi',
            name='tanggal_registrasi',
            field=models.DateField(auto_now=True),
        ),
    ]
