from django.contrib import admin
from django.contrib.admin import AdminSite
from .models import Paket, Pembayaran, Member, Wilayah, Registrasi
from django.contrib.auth.models import User, Group

class SaharaAdminSite(AdminSite):
    site_header = "Sahara Administrator"

admin_site = SaharaAdminSite(name='saharaadmin')


class AdminPaket(admin.ModelAdmin):
    pass
    #list_display = ('nama', 'status',)

class AdminPembayaran(admin.ModelAdmin):
    pass

class AdminMember(admin.ModelAdmin):
    pass
    #list_display = ('nama', 'wilayah', 'paket', 'pembayaran')
    #list_filter = ['wilayah', 'paket', 'pembayaran']

class AdminRegistrasi(admin.ModelAdmin):
    list_display = [
        'nomer_registrasi', 'tanggal_registrasi','nama','email', 'jenis_kelamin',
        'nomor_hp', 'pembayaran','wilayah', 'paket', 'status_member'
    ]
    list_filter = [
        'tanggal_registrasi', 'wilayah',
        'paket', 'pembayaran', 'jenis_kelamin'
    ]

class AdminWilayah(admin.ModelAdmin):
    pass

class AdminUserCustom(admin.ModelAdmin):
    pass

admin_site.register(User)
admin_site.register(Paket, AdminPaket)
admin_site.register(Pembayaran, AdminPembayaran)
admin_site.register(Member, AdminMember)
admin_site.register(Wilayah, AdminWilayah)
admin_site.register(Registrasi, AdminRegistrasi)

admin_site.register(Group)
