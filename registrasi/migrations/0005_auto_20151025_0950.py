# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registrasi', '0004_auto_20151024_2109'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sponsor',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('tanggal', models.DateField(auto_now_add=True)),
                ('nomor_member', models.ForeignKey(null=True, blank=True, to='registrasi.Member')),
            ],
            options={
                'verbose_name_plural': 'Sponsor',
            },
        ),
        migrations.RenameField(
            model_name='registrasi',
            old_name='nomer_registrasi',
            new_name='nomor_registrasi',
        ),
        migrations.AddField(
            model_name='sponsor',
            name='nomor_registrasi',
            field=models.ForeignKey(null=True, blank=True, to='registrasi.Registrasi'),
        ),
    ]
