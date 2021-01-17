from django.db import models
from django.utils import timezone
from ckeditor_uploader.fields import *
from mptt.models import MPTTModel,TreeForeignKey
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.
class Category(MPTTModel):
    check_status = (
        ('True','True'),
        ('False','False'),
    )
    parent = TreeForeignKey('self',related_name='childern',on_delete=models.CASCADE ,blank=True,null=True) # a category can have present in more than one parent or in just one parent e.g  Men's Fashion(Grand parent) > Men's clothing(parent) > T-Shirts(category)
    title = models.CharField(max_length=30)
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    status = models.CharField(max_length=20,choices=check_status) 
    slug = models.SlugField(blank=True,unique=True)
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class MPTTMeta:
        order_insertion_by = ['title']

    
    def __str__(self):
        full_path = [self.title]
        k = self.parent
        while k is not None:
            full_path.append(k.title)
            k = k.parent
        return '/'.join(full_path[::-1])

    def _get_unique_slug(self):
        slug = slugify(self.title)
        unique_slug = slug
        num = 1
        while Category.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug
 
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super().save(*args, **kwargs)
