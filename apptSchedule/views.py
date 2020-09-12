from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import ApptSchedule
from .serializers import ApptScheduleSerializer

# Create your views here.
class ApptScheduleList(ListCreateAPIView):
  queryset=ApptSchedule.objects.all()
  serializer_class = ApptScheduleSerializer

class ApptScheduleDetail (RetrieveUpdateDestroyAPIView):
  queryset=ApptSchedule.objects.all()
  serializer_class = ApptScheduleSerializer
