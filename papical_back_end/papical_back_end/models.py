from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.gis.db.models import PointField
from datetime import datetime, timedelta


class User(AbstractUser):

  GENDER_CHOICES = [
    ('M', 'Male'),
    ('F', 'Female'),
    ('NB', 'Non-Binary'),
    ('PN', 'Prefer not to say')
  ]

  email = models.EmailField(unique=True)
  location = models.CharField(max_length=30)
  date_of_birth = models.DateField(null=True, blank=True)
  gender = models.CharField(max_length=2, choices=GENDER_CHOICES)
  location = PointField(null=True, blank=True)


class Event(models.Model):
  name = models.CharField(max_length=255)
  start_time = models.TimeField()
  end_time = models.TimeField()
  description = models.TextField(null=True)
  creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_events')
  location = PointField(null=True, blank=True)

  def participants(self):
    return self.invitations.filter(lambda invitation: invitation.attending)


class Invitation(models.Model):

  INVITE_CHOICES = [
    ('A', 'Attending'),
    ('NA', 'Not Attending'),
  ]

  invitee = models.ForeignKey(User, on_delete=models.CASCADE, related_name='invitations')
  event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='invitations')
  attending = models.CharField(max_length=2, choices=INVITE_CHOICES, default='NA')


# Effectively the Tag pattern. Might try using a library here...
class Interest(models.Model):
  name = models.CharField(max_length=255)
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='interests')
  event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='interests')
  # Effectively "Tags"
  # manytomany (ForeignKey of event)
  # manytomany (ForeignKey of user)
