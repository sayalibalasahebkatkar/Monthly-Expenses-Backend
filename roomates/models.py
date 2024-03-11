from django.db import models
import uuid
from datetime import date

class Roomate(models.Model):
    user_id = models.CharField(max_length=100,unique=True)
    email_id = models.EmailField()
    password = models.CharField(max_length=100)
    token = models.UUIDField(default=uuid.uuid4,editable=False,unique=True,max_length=16)

class Team(models.Model):
    team_id = models.UUIDField(default=uuid.uuid4,editable=False,unique=True,max_length=16)
    user_id = models.ManyToManyField(Roomate, related_name='teams')
    team_name = models.CharField(max_length=255)

class Transaction(models.Model):
    user = models.ForeignKey(Roomate, on_delete=models.DO_NOTHING)
    team = models.ForeignKey(Team, on_delete=models.DO_NOTHING)
    amount = models.FloatField()
    description = models.TextField(default='')
    date = models.DateField(default=date.today)




