from django.db import models

# Create your models here.
class TimeSheet(models.Model):
  user = models.ForeignKey('auth.User')
  title = models.CharField(max_length=200)
  description = models.TextField()
  duration = models.DurationField()

  def __str__(self):
    return "%s worked on %s for %s" % (self.user.username, self.title, self.duration)
