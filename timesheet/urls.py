from django.conf.urls import url
from . import views

urlpatterns = [
  url(r'^$', views.timesheet_list, name='timesheet_list'),
  url(r'^new/$', views.timesheet_new, name='timesheet_new'),
  url(r'^(?P<pk>\d+)/$', views.timesheet_detail, name='timesheet_detail'),
  url(r'^(?P<pk>\d+)/edit/$', views.timesheet_edit, name='timesheet_edit'),
]
