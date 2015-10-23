from django.db import models
from django.contrib.auth.models import User


class Paket(models.Model):
    """
    Model Class Paket.

    adalah tabel registrasi_paket yang digunakan
    untuk menyimpan data-data berupa jenis-jenis paket.
    """
    kode_paket = models.CharField(max_length=4, primary_key=True)
    nama_paket = models.CharField(max_length=30)
    keterangan_paket = models.TextField()
    status_paket = models.BooleanField()
    harga_paket = models.IntegerField()

    def __str__(self):
        """
        Mengembalikan string 'nama_paket'
        ke halaman html.
        """
        return self.nama_paket

    class Meta:
        verbose_name = "Paket"
        verbose_name_plural = "Master Paket"


class Pembayaran(models.Model):
    """
    Model Class Pembayaran.

    adalah tabel registrasi_pembayaran yang digunakan
    untuk menyimpan data-data berupa jenis-jenis pembayaran.
    """
    kode_pembayaran = models.CharField(max_length=4, primary_key=True)
    jenis_pembayaran = models.CharField(max_length=30)

    def __str__(self):
        """
        Mengembalikan string 'jenis_pembayaran'
        ke halaman html.
        """
        return self.jenis_pembayaran

    class Meta:
        verbose_name_plural = "Master Jenis Pembayaran"

class Wilayah(models.Model):
    """
    Model Class Wilayah.

    adalah tabel registrasi_wilayah
    yang digunakan untuk menyimpan data wilayah.
    """
    kode_wilayah = models.CharField(max_length=4, primary_key=True)
    nama_wilayah = models.CharField(max_length=100, unique=True)

    def __str__(self):
        """
        Mengembalikan string 'nama_wilayah'
        ke halaman html.
        """
        return self.nama_wilayah

    class Meta:
        verbose_name_plural = "Master Wilayah"


class Registrasi(models.Model):
    """
    Class untuk menyimpan data registrasi.

    registrasi digunakan untuk menyimpan
    data calon member. calon member yang
    sudah di ceklis statusnya menjadi True
    akan menjadi member atau anggota.
    """
    nomer_registrasi = models.CharField(max_length=10, unique=True, blank=True, null=True)
    nama = models.CharField(max_length=120)
    alamat = models.TextField()
    wilayah = models.ForeignKey(Wilayah)
    email = models.EmailField()
    nomor_hp = models.CharField(max_length=16)
    tempat_lahir = models.CharField(max_length=30)
    tanggal_lahir = models.DateField()
    JENKEL = (
        ('P', 'Pria'),
        ('W', 'Wanita'),
    )
    jenis_kelamin = models.CharField(max_length=1, choices=JENKEL, default='P')
    paket = models.ForeignKey(Paket)
    pembayaran = models.ForeignKey(Pembayaran)
    status = models.BooleanField(default=False, blank=True)
    tanggal_registrasi = models.DateField(auto_now=True)

    def __str__(self):
        """
        Mengembalikan string 'nama' dari calon member
        ke halaman html.
        """
        return self.nama

    def status_member(self):
        """
        Mengembalikan nilai bool untuk status calon member.
        """
        return self.status

    status_member.boolean = True
    status_member.short_description = "SUDAH MENJADI MEMBER ?"

    class Meta:
        verbose_name = "Calon Member"
        verbose_name_plural = "Data Calon Member (Registrasi)"

class Member(models.Model):
    """
    Class untuk data member.

    seorang calon member yang sudah melakukan
    registrasi dan sudah mendapat persetujuan
    oleh admin akan menjadi anggota member.
    """
    nomor_member = models.CharField(max_length=11, primary_key=True)
    registrasi = models.OneToOneField(Registrasi)


    def __str__(self):
        """
        Mengembalikan string 'nama_member'
        ke halaman html.
        """
        return self.nama_member

    class Meta:
        verbose_name_plural = "Data Member"

