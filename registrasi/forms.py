from django.forms import ModelForm
from django.forms import Textarea
from django.forms import TextInput
from django.forms import Select
from django.forms import EmailInput
from django.forms import DateInput
from django.forms import RadioSelect
from django import forms

from .models import Registrasi
from .helpers.validation import validate_sponsor


class RegistrasiForm(ModelForm):
    """
    Form untuk registrasi member.
    """
    sponsor = forms.CharField(required=False,
        widget=TextInput(attrs={'class':'form-control'}),
        validators=[validate_sponsor])

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
            'nomor_registrasi','status',
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
            'jenis_kelamin': RadioSelect(attrs={'class':''}),
            'paket': Select(attrs={'class':'form-control'}),
            'pembayaran': Select(attrs={'class':'form-control'}),
        }
