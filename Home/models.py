from django.db import models
from django.utils import timezone

# Create your models here.
class Setting(models.Model):
    is_status = (
        ('True','True'),
        ('False','False'),
    )
    title = models.TextField(blank=True)
    keywords = models.TextField(blank=True)
    description = models.TextField(blank=True)
    company = models.CharField(max_length=255,blank=True)
    address = models.TextField(blank=True)
    phone = models.CharField(max_length=30,blank=True)
    fax = models.CharField(max_length=100,blank=True)
    email = models.CharField(max_length=30,blank=True)
    smtpserver = models.CharField(max_length=225,blank=True)
    smtpemail = models.CharField(max_length=225,blank=True)
    smtppassword = models.CharField(max_length=225,blank=True)
    smtpport = models.CharField(max_length=225,blank=True)
    icon = models.ImageField(blank=True,upload_to='images')
    facebook = models.CharField(max_length=225,blank=True)
    instagram = models.CharField(max_length=225,blank=True)
    twitter = models.CharField(max_length=225,blank=True)
    status = models.CharField(max_length=225,blank=True,choices=is_status)
    datetime = models.DateTimeField('date_created', default=timezone.now(), blank=False)

    def __str__(self):
        return self.title

