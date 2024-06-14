# payslip_app/views.py
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import Payslip
from .serializer import PayslipSerializer


class PayslipUploadView(generics.CreateAPIView):
    queryset = Payslip.objects.all()
    serializer_class = PayslipSerializer


class PayslipListView(generics.ListAPIView):
    queryset = Payslip.objects.all()
    serializer_class = PayslipSerializer
    permission_classes = [IsAuthenticated]


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_payslips(request):
    payslips = Payslip.objects.all()
    serializer = PayslipSerializer(payslips, many=True)
    return Response(serializer.data)
