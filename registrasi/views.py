from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.utils import timezone
from django.contrib import messages
import time

from .forms import RegistrasiForm
from .helpers.generate_id import Generator
from .models import Sponsor
from .models import Registrasi
from .models import Member

class ViewBaseRegistrasi(object):
    """
    class ini seperti halnya controller. class ini
    digunakan untuk menampung method request yang bertanggung
    jawab meresponse permintaan user atau client.

    untuk digunakan di registrasi/urls.py cukup dengan::

        # http://localhost:8000/
        url(r'^$', ViewBaseRegistrasi().home, name='home'),

    """
    def home(self, request):
        context = {}
        template = 'registrasi/home.html'
        return render(request, template, context)


class ViewRegistrasi(object):

    def registrasi(self, request):
        if request.method == 'POST':
            form = RegistrasiForm(request.POST)
            #print(type(form.data.get('sponsor')))
            #print(dir(form))
            if form.is_valid():
                nomor_member_sponsor = form.data.get('sponsor')
                register = form.save(commit=False)
                register.nomor_registrasi = Generator().generate_from_date()
                register.tanggal_registrasi = timezone.now()
                register.save()
                self.__save_sponsor(nomor_member_sponsor, register)
                messages.info(request, 'Terimakasih telah registrasi.')
                return HttpResponseRedirect(reverse('registrasi:registrasi-member'))
        else:
            form = RegistrasiForm()

        context = {'form':form}
        template = 'registrasi/register.html'
        return render(request, template, context)

    def __save_sponsor(self, nomor_member_sponsor, register):
        # dapatkan objek member dari registrasi

        object_registrasi = Registrasi.objects.get(nomor_registrasi=register.nomor_registrasi)
        sponsor = Sponsor()
        if nomor_member_sponsor:
            object_member = Member.objects.get(nomor_member=nomor_member_sponsor)
            sponsor.nomor_member = object_member
            sponsor.nomor_registrasi = object_registrasi
        else:
            sponsor.nomor_registrasi = object_registrasi

        sponsor.save()
