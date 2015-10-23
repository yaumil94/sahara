from django.forms import ModelForm
from django.forms import Textarea
from django.forms import TextInput
from django.forms import Select
from django.forms import EmailInput
from django.forms import DateInput
from django.forms import RadioSelect

from .models import Registrasi

'''
class FormRegistrasi(forms.Form):
    nomer = forms.CharField(required=False,max_length=5,label='Nomer Urut', widget=forms.TextInput(attrs={'class':'form-control'}))
    nama = forms.CharField(max_length=30, label='Nama', widget=forms.TextInput(attrs={'class':'form-control'}))
    alamat = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))
    wilayah = forms.ChoiceField(label='kota', choices=wilayah_choices(), widget=forms.Select(attrs={'class':'form-control'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class':'form-control'}))
    handphone = forms.CharField(label='Nomer Handphone', max_length=16, widget=forms.TextInput(attrs={'class':'form-control'}))
    tempat_lahir = forms.CharField(label='Tempat Lahir', max_length=30, widget=forms.TextInput(attrs={'class':'form-control'}))
    tanggal_lahir = forms.CharField(label='Tanggal Lahir', widget=forms.DateInput(attrs={'class':'form-control'}))
    pembayaran = forms.ChoiceField(choices=pembayaran_choices(), widget=forms.Select(attrs={'class':'form-control'}))
    jenis_kelamin = forms.ChoiceField(choices=gender_choices(), widget=forms.RadioSelect(attrs={'class':'form-control'}))
    paket_sahara = forms.ChoiceField(choices=paket_choices(), widget=forms.Select(attrs={'class':'form-control'}))
'''

class RegistrasiForm(ModelForm):

    class Meta:
        model = Registrasi
        # field wajib tampil
        fields = [
            'nama', 'alamat', 'wilayah',
            'email', 'nomor_hp', 'tempat_lahir',
            'tanggal_lahir', 'jenis_kelamin','paket', 'pembayaran'
        ]
        # field yang tidak ditampilkan
        exlcude = [
            'nomer_registrasi','status',
            'tanggal_registrasi'
        ]
        # widget
        widgets = {
            'nama': TextInput(attrs={'class':'form-control'}),
            'alamat': Textarea(attrs={'class':'form-control'}),
            'wilayah': Select(attrs={'class':'form-control'}),
            'email': EmailInput(attrs={'class':'form-control'}),
            'nomor_hp': TextInput(attrs={'class':'form-control'}),
            'tempat_lahir': TextInput(attrs={'class':'form-control'}),
            'tanggal_lahir': DateInput(attrs={'class':'form-control'}),
            'jenis_kelamin': RadioSelect(attrs={'class':'form-control'}),
            'paket': Select(attrs={'class':'form-control'}),
            'pembayaran': Select(attrs={'class':'form-control'}),
        }
