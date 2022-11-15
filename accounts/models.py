from django.db import models
from django.contrib.auth.models import User

class UserContact(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    instagram = models.TextField(default="")
    phone_number = models.IntegerField(default= 0 )

   


