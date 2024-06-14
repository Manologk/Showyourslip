from rest_framework import serializers
from .models import Payslip


class PayslipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payslip
        fields = '__all__'

    def validate(self, data):
        if 'file' not in data:
            data['file'] = None
        return data
