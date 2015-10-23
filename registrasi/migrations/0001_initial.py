# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('nomor_member', models.CharField(primary_key=True, serialize=False, max_length=11)),
            ],
            options={
                'verbose_name_plural': 'Data Member',
            },
        ),
        migrations.CreateModel(
            name='Paket',
            fields=[
                ('kode_paket', models.CharField(primary_key=True, serialize=False, max_length=4)),
                ('nama_paket', models.CharField(max_length=30)),
                ('keterangan_paket', models.TextField()),
                ('status_paket', models.BooleanField()),
                ('harga_paket', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'Master Paket',
                'verbose_name': 'Paket',
            },
        ),
        migrations.CreateModel(
            name='Pembayaran',
            fields=[
                ('kode_pembayaran', models.CharField(primary_key=True, serialize=False, max_length=4)),
                ('jenis_pembayaran', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name_plural': 'Master Jenis Pembayaran',
            },
        ),
        migrations.CreateModel(
            name='Registrasi',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('nomer_registrasi', models.CharField(max_length=10, unique=True)),
                ('nama', models.CharField(max_length=120)),
                ('alamat', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('nomor_hp', models.CharField(max_length=16)),
                ('tempat_lahir', models.CharField(max_length=30)),
                ('tanggal_lahir', models.DateField()),
                ('status', models.BooleanField(default=False)),
                ('tanggal_registrasi', models.DateField(auto_now_add=True)),
                ('paket', models.ForeignKey(to='registrasi.Paket')),
                ('pembayaran', models.ForeignKey(to='registrasi.Pembayaran')),
            ],
            options={
                'verbose_name_plural': 'Data Calon Member (Registrasi)',
            },
        ),
        migrations.CreateModel(
            name='Wilayah',
            fields=[
                ('kode_wilayah', models.CharField(primary_key=True, serialize=False, max_length=4)),
                ('nama_wilayah', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Master Wilayah',
            },
        ),
        migrations.AddField(
            model_name='registrasi',
            name='wilayah',
            field=models.ForeignKey(to='registrasi.Wilayah'),
        ),
        migrations.AddField(
            model_name='member',
            name='registrasi',
            field=models.OneToOneField(to='registrasi.Registrasi'),
        ),
    ]
