from django.urls import path

from .views import MedScheduleList, MedScheduleDetail

urlpatterns = [
  path('', MedScheduleList.as_view(), name='MedSchedule_list'),
  path('<int:pk>/', MedScheduleDetail.as_view(), name='MedSchedule_detail')
]