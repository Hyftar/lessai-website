from django.shortcuts import render, get_object_or_404
from .models import TimeSheet

# Create your views here.
def home(request):
  return render(request, 'timesheet/home.html')

def timesheet_list(request):
  timesheets = TimeSheet.objects.order_by('creationtime')
  return render(request, 'timesheet/timesheet_list.html', {'timesheets': timesheets})

def timesheet_detail(request, pk):
  timesheet = get_object_or_404(TimeSheet, pk=pk)
  pretty_duration = timesheet.PrettyTime()
  return render(request, 'timesheet/timesheet_detail.html', {'timesheet': timesheet, 'pretty_duration': pretty_duration})
