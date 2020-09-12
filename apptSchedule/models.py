from django.db import models

# Create your models here.
from user.models import CustomUser
from clinicInformation.models import DoctorClinic

class ApptSchedule(models.Model):
  user = models.ForeignKey(CustomUser, default = 1, verbose_name = "username", on_delete = models.SET_DEFAULT)
  timeOfAppt = models.DateTimeField(auto_now=True, auto_now_add = False)
  doctor_name = models.ForeignKey(DoctorClinic, default = 1, verbose_name = "doctorName", on_delete = models.SET_DEFAULT)
  duration = models.TimeField(verbose_name="min")
  attended = models.BooleanField(default=False)
  user_apptSchedule=models.CharField(max_length=64)
  def __str__(self):
    return self.user_apptSchedule
