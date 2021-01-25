from django.db import models
from django.contrib.auth.models import User
from Products.models import Varient,Product
from seller.models import Seller

# Create your models here.
class Orders(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,blank=True,null=True)
    varient = models.ForeignKey(Varient,on_delete=models.CASCADE,blank=True,null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    seller = models.ForeignKey(Seller,on_delete=models.CASCADE,blank=True,null=True)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        if self.varient is not None:
            return self.varient.title

    def save(self, *args, **kwargs):
        if  self.product is not None:
            self.seller = self.product.seller
            super(Orders, self).save(*args, **kwargs)

    @property
    def amount(self):
        if self.varient is not None:
            return  int(self.quantity) * int(self.varient.price)