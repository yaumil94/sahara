from django.db import models
from django.contrib.auth.models import User


class Paket(models.Model):
    """
    Menyimpan data Paket. tabel untuk model ini
    adalah **registrasi_paket** yang dijadikan
    FK oleh `registrasi.Registrasi`.
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
    Menyimpan data Jenis Pembayaran. tabel untuk model ini
    adalah **registrasi_pembayaran** yang dijadikan
    FK oleh `registrasi.Registrasi`.
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
    Menyimpan data Wilayah. tabel untuk model ini
    adalah **registrasi_wilayah** yang dijadikan
    FK oleh `registrasi.Registrasi`.
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
        """
        Merepresentasikan nama models
        di aplikasi pada halaman administrator.
        """
        verbose_name_plural = "Master Wilayah"



class Registrasi(models.Model):
    """
    Class untuk menyimpan data registrasi.

    registrasi digunakan untuk menyimpan
    data calon member. calon member yang
    sudah di ceklis statusnya menjadi True
    akan menjadi member atau anggota.
    """
    nomor_registrasi = models.CharField(max_length=10, unique=True, blank=True, null=True)
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

    def list_display_sponsor(self):
        """
        Mengembalikan nilai nomor_member sebagai
        sponsor user yang masih dalam status register.
        """
        try:
            sponsor = Sponsor.objects.get(nomor_registrasi=self)
            if not sponsor.nomor_member:
                return "--"
            else:
                return sponsor.nomor_member
        except Sponsor.DoesNotExist:
            return "--"
    list_display_sponsor.short_description = "Sponsor"

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
    nomor_member = models.CharField(max_length=12, primary_key=True)
    registrasi = models.ForeignKey(Registrasi)
    #tanggal_menjadi_member = models.DateTimeField()


    def __str__(self):
        """
        Mengembalikan string 'nama_member'
        ke halaman html.
        """
        return self.nomor_member

    def get_nomor_registrasi(self):
        return self.registrasi.nomor_registrasi
    get_nomor_registrasi.short_description = "Nomor Registrasi"

    def list_display_banyak_member(self):
        return self.sponsor_set.count()
    list_display_banyak_member.short_description = "Jumlah Pengikut Member"

    def list_display_sponsor(self):
        """
        Mengembalikan nilai nomor_member sebagai
        sponsor user.
        """
        try:
            sponsor = Sponsor.objects.get(nomor_registrasi=self.registrasi)
            if not sponsor.nomor_member:
                return "--"
            else:
                return sponsor.nomor_member
        except Sponsor.DoesNotExist:
            return "--"
    list_display_sponsor.short_description = "Di Sponsori oleh"

    class Meta:
        verbose_name_plural = "Data Member"


class Sponsor(models.Model):
    nomor_registrasi = models.ForeignKey(Registrasi, blank=True, null=True)
    nomor_member = models.ForeignKey(Member, help_text="Nomor ini sebagai nomor Sponsor Member", blank=True, null=True)
    tanggal = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nomor_registrasi.nama

    class Meta:
        verbose_name_plural = "Sponsor"