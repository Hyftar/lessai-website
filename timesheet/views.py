from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import TimeSheet
from .forms import TimeSheetForm
import django.http

# Create your views here.
def home(request):
  return render(request, 'timesheet/home.html')

# def register(request):
#   if request.method == 'POST':
#       uf = UserForm(request.POST, prefix='user')
#       if uf.is_valid():
#         user = uf.save()
#         return django.http.HttpResponseRedirect('home')
#   else:
#       uf = UserForm(prefix='user')
#   return django.shortcuts.render_to_response('register.html', dict(userform=uf, context_instance=django.template.RequestContext(request)))

def timesheet_list(request):
  timesheets = TimeSheet.objects.order_by('creationtime').reverse()
  return render(request, 'timesheet/timesheet_list.html', {'timesheets': timesheets})

def timesheet_detail(request, pk):
  timesheet = get_object_or_404(TimeSheet, pk=pk)
  return render(request, 'timesheet/timesheet_detail.html', { 'timesheet': timesheet })

@login_required
def timesheet_new(request):
  if request.method == "POST":
    form = TimeSheetForm(request.POST)
    if (form.is_valid()):
      timesheet = form.save(commit=False)
      timesheet.user = request.user
      timesheet.creationtime = timezone.now()
      timesheet.save()
      return redirect('timesheet_detail', pk=timesheet.pk)
  else:
    form = TimeSheetForm()
  return render(request, 'timesheet/timesheet_edit.html', {'form': form})

@login_required
def timesheet_edit(request, pk):
  timesheet = get_object_or_404(TimeSheet, pk=pk)
  if request.method == "POST":
    form = TimeSheetForm(request.POST, instance=timesheet)
    if (form.is_valid()):
      timesheet = form.save(commit=False)
      timesheet.user = request.user
      timesheet.creationtime = timezone.now()
      timesheet.save()
      return redirect('timesheet_detail', pk=timesheet.pk)
  else:
    form = TimeSheetForm(instance=timesheet)
  return render(request, 'timesheet/timesheet_edit.html', {'form': form })

@login_required
def account(request):
  timesheets = TimeSheet.objects.filter(user=request.user)
  return render(request, 'registration/account.html', { 'timesheets': timesheets })
