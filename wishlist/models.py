from django.db import models
from Products.models import Varient,Product
from django.contrib.auth.models import User

# Create your models here.
class Wishlist(models.Model):
    varient = models.ForeignKey(Varient,on_delete=models.CASCADE,related_name='product_varient') 
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='product_name') 
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)

    def __str__(self):
        return self.varient.title


