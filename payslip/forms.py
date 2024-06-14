from django import forms
from .models import Payslip


class PayslipForm(forms.ModelForm):
    class Meta:
        model = Payslip
        fields = ['file']