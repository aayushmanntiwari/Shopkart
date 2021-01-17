from django.db import models
from django.contrib.auth.models import User,Group

# Create your models here.
class ExtendeRegisterUser(models.Model):
    mobilenumber = models.CharField(max_length=20)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
