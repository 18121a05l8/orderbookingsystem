# Create your models here.
from django.db import models
class Job(models.Model):
    name = models.CharField(max_length=200)
class User(models.Model):
    name = models.CharField(max_length=200)
class Charge(models.Model):
    HARDWARE = 'hw'
    SOFTWARE = 'sw'
    TYPE_CHOICES = (
        (HARDWARE, 'Hardware'),
        (SOFTWARE, 'Software'),
    )
    type = models.CharField(choices=TYPE_CHOICES, max_length=2)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    month = models.DateField()
    user = models.ForeignKey(User)
    job = models.ForeignKey(Job, null=True, blank=True)