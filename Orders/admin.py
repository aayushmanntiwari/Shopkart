from django.contrib import admin
from .models import Orders

# Register your models here.
class OrderAdmin(admin.ModelAdmin):
    list_display = ['varient','user','quantity','amount']
admin.site.register(Orders,OrderAdmin)
