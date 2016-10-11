from django.db import models

# Create your models here.
class TimeSheet(models.Model):
  user = models.ForeignKey('auth.User')
  title = models.CharField(max_length=200)
  description = models.TextField()
  duration = models.DurationField()

  def __str__(self):
    return "%s worked on %s for %s" % (self.user.username, self.title, self.PretyTime())

  def PrettyTime(self):
    time = self.duration.seconds
    out = ''
    days = int(time / (3600 * 24))
    time -= days * (3600 * 24)
    hours = int(time / 3600)
    time -=  hours * 3600
    minutes = int(time / 60)
    time -= minutes * 60
    seconds = int(time)

    if (days > 0):
      out += str(days) + ' day' + ('s ' if (days > 1) else ' ')
    if (hours > 0):
      out += str(hours) + ' hour' + ('s ' if (hours > 1) else ' ')
    if (minutes > 0):
      out += str(minutes) + ' minute' + ('s ' if (minutes > 1) else ' ')
    if (seconds > 0):
      out += str(seconds) + ' second' + ('s ' if (seconds > 1) else ' ')

    return out.strip()
