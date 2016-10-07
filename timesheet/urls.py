from django.conf.urls import url
from . import views

urlpatterns = [
  url(r'^$', views.timesheet_list, name='timesheet_list')
]
