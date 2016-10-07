from django.shortcuts import render

# Create your views here.
def timesheet_list(request):
  return render(request, 'timesheet/timesheet_list.html', {})
