from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Seller(models.Model):
    mobilenumber = models.CharField(max_length=10,null=True,blank=False)
    firstname = models.CharField(max_length=255,null=True,blank=False) 
    lastname = models.CharField(max_length=255,null=True,blank=False) 
    seller = models.ForeignKey(User,blank=True,null=True,on_delete=models.CASCADE)

    def __str__(self):
        if self.firstname!="" and self.lastname!="":
            return self.firstname+self.lastname
        else:
            return self.firstname
