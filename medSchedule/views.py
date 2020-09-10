from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import MedSchedule
from .serializers import MedScheduleSerializer

# Create your views here.
class MedScheduleList(ListCreateAPIView):
  queryset = MedSchedule.objects.all()
  serializer_class = MedScheduleSerializer

class MedScheduleDetail(RetrieveUpdateDestroyAPIView):
  queryset = MedSchedule.objects.all()
  serializer_class = MedScheduleSerializer