from django.urls import path
from .views import ApptScheduleList, ApptScheduleDetail

urlpatterns = [
  path('', ApptScheduleList.as_view(), name = 'ApptSchedule_list'),
  path ('<int:pk>/', ApptScheduleDetail.as_view(), name='ApptSchedule_detail')
]