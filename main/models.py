from typing import Text
from django.db import models

class ToDo(models.Model):
    text = models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add=True)
    is_closed = models.BooleanField(default=False)
    is_favorite = models.BooleanField(default=False)

class toMeet(models.Model):
    persone = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=12)
    date_of_meeting = models.DateTimeField(auto_now=True)
    is_closed = models.BooleanField(default=False)
    is_favorite = models.BooleanField(default=False)