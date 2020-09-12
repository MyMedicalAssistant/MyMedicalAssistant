from django.urls import path

from .views import DoctorClinicList, DoctorClinicDetail

urlpatterns = [
  path('', DoctorClinicList.as_view(), name='DoctorClinic_list'),
  path('<int:pk>/', DoctorClinicDetail.as_view(), name='DoctorClinic_detail')
]