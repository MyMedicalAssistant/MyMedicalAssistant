from rest_framework import serializers

from .models import ApptSchedule

class ApptScheduleSerializer(serializers.ModelSerializer):

  class Meta:
    model = ApptSchedule
    fields = (
      'id',
      'user',
      'timeOfAppt',
      'doctor_name',
      'duration',
      'attended',
      'user_apptSchedule',
      )