from django.contrib import admin
from django.contrib.admin import AdminSite
from .models import Paket, Pembayaran, Member, Wilayah, Registrasi, Sponsor
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
    list_display = (
        'nomor_member', 'registrasi', 'list_display_sponsor',
        'get_nomor_registrasi', 'list_display_banyak_member',)
    #list_filter = ['wilayah', 'paket', 'pembayaran']

class AdminRegistrasi(admin.ModelAdmin):
    list_display = [
        'nomor_registrasi', 'list_display_sponsor','tanggal_registrasi','nama','email', 'jenis_kelamin',
        'nomor_hp', 'pembayaran','wilayah', 'paket', 'status_member'
    ]
    list_filter = [
        'tanggal_registrasi', 'wilayah',
        'paket', 'pembayaran', 'jenis_kelamin'
    ]

    actions = ['register_to_member', 'export_as_json']

    def register_to_member(self, request, queryset):
        data_register = queryset.all()
        # ubah menjadi status true
        data_register.update(status=True)
        for data_calon_member in data_register:
            nomer_calon_member = "M" + str(data_calon_member.nomor_registrasi)
            member = Member()
            member.nomor_member = nomer_calon_member
            member.registrasi = data_calon_member
            member.save()
    register_to_member.short_description = "Ubah Menjadi Member"

    def cetak_laporan(self, request):
        """
        view cetak laporan, kustomisasi view di admin
        buat bikin cetak laporan.
        """
        from django.http import HttpResponseRedirect
        from django.core.urlresolvers import reverse
        print("cetak laporan sedang berjalan!")
        return HttpResponseRedirect(
                reverse("admin:registrasi_registrasi_changelist")
        )

    def get_urls(self):
        """
        get_urls method overriding dari class ModelAdmin
        yang digunakan untuk mendapatkan URL, untuk
        mengkustom view dan url pada halaman admin.
        """
        from django.conf.urls import patterns, url
        urls = super(AdminRegistrasi, self).get_urls()
        # saat mengunjungi 'update_feeds' url maka
        # view yang gue custom melalui method admin_view
        # bakal kepangil
        my_urls = patterns('',
            url(
                r'cetak-laporan',
                self.admin_site.admin_view(self.cetak_laporan),
                name='cetak_laporan',
            ),
        )
        return my_urls + urls

class AdminWilayah(admin.ModelAdmin):
    pass

class AdminUserCustom(admin.ModelAdmin):
    pass

class AdminSponsor(admin.ModelAdmin):
    pass

admin_site.register(User)
admin_site.register(Paket, AdminPaket)
admin_site.register(Pembayaran, AdminPembayaran)
admin_site.register(Member, AdminMember)
admin_site.register(Wilayah, AdminWilayah)
admin_site.register(Registrasi, AdminRegistrasi)
admin_site.register(Sponsor, AdminSponsor)
admin_site.register(Group)
