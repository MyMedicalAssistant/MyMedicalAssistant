
# Create your models here.
from django.db import models
from user.models import CustomUser
from clinicInformation.models import DoctorClinic

class MedSchedule(models.Model):
  user = models.ForeignKey(CustomUser, default = 1, verbose_name="username", on_delete = models.SET_DEFAULT)
  doctor_name = models.ForeignKey(DoctorClinic, default = 1, verbose_name="doctor_name", on_delete=models.SET_DEFAULT)
  medication = models.CharField(max_length=64)
  hours = models.IntegerField()
  dosage = models.CharField(max_length=256)
  inventory = models.IntegerField()
  start = models.DateTimeField(auto_now=False, auto_now_add=False)
  last = models.DateTimeField(auto_now=False, auto_now_add=False)
  next_dosage = models.DateTimeField(auto_now=False, auto_now_add=False)
  end = models.DateTimeField(auto_now=False, auto_now_add=False)
  user_id_medication = models.CharField(max_length=64)
  def __str___(self):
    return self.user_id_medication