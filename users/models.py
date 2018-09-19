from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your models here.
class UserProfile(models.Model):
    title   = models.CharField(max_length=100, default='')
    about   = models.TextField(max_length=100, default='')
    city    = models.CharField(max_length=100, default='')
    phone   = models.IntegerField(default=0)
    website = models.URLField(default='')

    def __str__(self):
        return self.title