from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class KOMatch (models.Model):
    local = models.TextField()
    local_score = models.IntegerField()
    visitor = models.TextField()
    visitor_score = models.IntegerField()
    user_id = models.IntegerField()
    match_number = models.IntegerField()
    round = models.IntegerField()
    qualified = models.TextField(default="")
    looser = models.TextField(default="")