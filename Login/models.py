from django.db import models
from django.contrib.auth.models import User,Group


# Create your models here.
class Failed(models.Model):
    count = models.IntegerField(default=0)
    user = models.OneToOneField(User,on_delete=models.CASCADE)