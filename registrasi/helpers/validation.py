from django.core.exceptions import ValidationError
from ..models import Member


def validate_sponsor(value):
    """
    Memvalidasi apakah nomor_member (sebagai sponsor)
    ada di dalam Member.

    :param value: nilai nomor_member yang dijadikan sponsor
    :type value: String nomer_member
    :return: void

    :Contoh: **registrasi/forms.py**

    >>> from .helpers.validation import validate_sponsor
    >>> sponsor = forms.CharField(required=False,
            widget=TextInput(attrs={'class':'form-control'}),
            validators=[validate_sponsor])
    """
    try:
        if value:
            nomor_member = Member.objects.get(nomor_member=value)
        else:
            pass
    except Member.DoesNotExist:
        raise ValidationError('sponsor %s tidak terdaftar' % value)
