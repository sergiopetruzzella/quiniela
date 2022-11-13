from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Match(models.Model):
    local = models.TextField()
    local_score = models.IntegerField()
    visitor = models.TextField()
    visitor_score = models.IntegerField()
    user_id = models.IntegerField()
    match_number = models.IntegerField()


class RealScore(models.Model):
    local_score = models.IntegerField()
    visitor_score = models.IntegerField()

class UserScore(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    points = models.IntegerField()