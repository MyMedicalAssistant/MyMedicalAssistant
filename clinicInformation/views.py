from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateAPIView
from .models import DoctorClinic
from .serializers import DoctorClinicSerializer

# Create your views here.
class DoctorClinicList (ListCreateAPIView):
  queryset = DoctorClinic.objects.all()
  serializer_class=DoctorClinicSerializer

class DoctorClinicDetail (RetrieveUpdateAPIView):
  queryset = DoctorClinic.objects.all()
  serializer_class = DoctorClinicSerializer
