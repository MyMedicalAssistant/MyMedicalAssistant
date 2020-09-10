from rest_framework import serializers

from .models import MedSchedule

class MedScheduleSerializer(serializers.ModelSerializer):

  class Meta:
    model = MedSchedule
    fields = (
      'id',
      'user',
      'medication',
      'hours',
      'dosage',
      'inventory',
      'start',
      'last',
      'next_dosage',
      'end',
      'user_id_medication'
      )