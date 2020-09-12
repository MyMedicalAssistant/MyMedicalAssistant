from rest_framework import serializers

from .models import DoctorClinic

class DoctorClinicSerializer(serializers.ModelSerializer):

  class Meta:
    model = DoctorClinic
    fields = (
      'id',
      'user',
      'doctor_name',
      'specialty',
      'clinic_name',
      'clinic_street',
      'clinic_city',
      'clinic_state',
      'clinic_country',
      'clinic_zipcode',
      'doctor_id'
      )