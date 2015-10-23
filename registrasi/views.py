from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.utils import timezone
from django.contrib import messages
import time

from .forms import RegistrasiForm
from .helpers.generate_id import Generator

class ViewBaseRegistrasi(object):

    def home(self, request):
        context = {}
        template = 'registrasi/home.html'
        return render(request, template, context)


class ViewRegistrasi(object):

    def registrasi(self, request):
        if request.method == 'POST':
            form = RegistrasiForm(request.POST)
            if form.is_valid():
                register = form.save(commit=False)
                register.nomer_registrasi = Generator().generate_from_date()
                register.tanggal_registrasi = timezone.now()
                register.save()
                messages.info(request, 'Terimakasih telah registrasi.')
                return HttpResponseRedirect(reverse('registrasi:registrasi-member'))
        else:
            form = RegistrasiForm()

        context = {'form':form}
        template = 'registrasi/register.html'
        return render(request, template, context)
