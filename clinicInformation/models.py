from django.db import models

# Create your models here
from user.models import CustomUser


class DoctorClinic(models.Model):
  user = models.ForeignKey(CustomUser, default = 1, verbose_name="username", on_delete = models.SET_DEFAULT)
  doctor_name = models.CharField(max_length=256)
  specialty = models.CharField(max_length=100)
  clinic_name = models.CharField(max_length=256)
  clinic_street= models.CharField(max_length=1000)
  clinic_city = models.CharField(max_length=256)
  clinic_state=models.CharField(max_length=200)
  clinic_country = models.CharField(max_length=200)
  clinic_zipcode = models.IntegerField()
  doctor_id = models.CharField(max_length=64)
  def __str__(self):
    return self.doctor_id
