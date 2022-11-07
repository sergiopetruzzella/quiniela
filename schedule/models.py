from django.db import models

# Create your models here.
class Match(models.Model):
    local = models.TextField()
    local_score = models.IntegerField()
    visitor = models.TextField()
    visitor_score = models.IntegerField()
    user_id = models.IntegerField()
    match_number = models.IntegerField()

class Schedule(models.Model):
    match_1 = Match()
    match_2 = Match()
    match_3 = Match()
    match_4 = Match()
    match_5 = Match()
    match_6 = Match()