from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.gis.db.models import PointField
# from datetime import datetime, timedelta
from taggit.managers import TaggableManager


class User(AbstractUser):

  GENDER_CHOICES = [
    ('M', 'Male'),
    ('F', 'Female'),
    ('NB', 'Non-Binary'),
    ('PN', 'Prefer not to say')
  ]

  email = models.EmailField(unique=True)
  date_of_birth = models.DateField(null=True, blank=True)
  gender = models.CharField(max_length=2, choices=GENDER_CHOICES)
  location = PointField(null=True, blank=True)
  tag = TaggableManager(verbose_name="Interests", help_text="Separate each interest with a comma.", blank=True)
  picture = models.ImageField(upload_to='images/', null=True)

  def __str__(self):
    return f'{self.first_name} {self.last_name}'


class Hangout(models.Model):
  name = models.CharField(max_length=255)
  date = models.DateField()
  start_time = models.TimeField()
  end_time = models.TimeField()
  description = models.TextField(null=True)
  creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_hangouts')
  location = PointField(null=True, blank=True)
  tag = TaggableManager(verbose_name="Tags", help_text="Separate each tag with a comma.", blank=True)

  def __str__(self):
    return f'{self.name}: {self.description}'

  def participants(self):
    return self.invitations.filter(lambda invitation: invitation.attending)


class FreeTime(models.Model):
  date = models.DateField()
  start_time = models.TimeField()
  end_time = models.TimeField()
  available = models.BooleanField(default=True)
  creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='freetime')

  def __str__(self):
    return f'Available on {self.date} from {self.start_time} to {self.end_time}'


class Invitation(models.Model):

  INVITE_CHOICES = [
    ('A', 'Attending'),
    ('NA', 'Not Attending'),
  ]

  creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_invitations')
  invitee = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_invitations')
  hangout = models.ForeignKey(Hangout, on_delete=models.CASCADE, related_name='invitations')
  attending = models.CharField(max_length=2, choices=INVITE_CHOICES, default='NA')

  def __str__(self):
    return f'{self.invitee} has been invited to {self.hangout}'
