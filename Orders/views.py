from django.shortcuts import render,redirect
from django.http import *
from .models import Orders
from Category.models import Category
from django.contrib.auth.models import User,Group
from .models import Orders
from Products.models import Varient,Image,Size

# Create your views here.
def showcart(request):
    try:
        user = User.objects.get(username = request.user)
        orders = Orders.objects.filter(user_id  = user.id)
        varients_orders = Varient.objects.all()
        if len(orders)!=0:
            total_products_in_cart = len(orders)
        else:
            total_products_in_cart = 0
        if len(orders)!=0:
            total_amount = sum([int(val.amount) for val in orders])
        else:
            total_amount = 0
        show_shopcart = True
    except:
        show_shopcart = False
    parent = Category.objects.all()
    childrenn = Category.objects.filter(level=1)
    subchildrenn = Category.objects.filter(level=2)
    subsubchildrenn = Category.objects.filter(level=3)
    images = Image.objects.all()
    sizes = Size.objects.all()
    varients_orders = Varient.objects.all()
    return render(request,'index.html',{
        'showcart':True,
        'parent':parent,
        'childrenn':childrenn,
        'subchildrenn':subchildrenn,
        'subsubchildrenn':subsubchildrenn,
        'shownavbar':True,
        'orders':orders,
        'images':images,
        'sizes':sizes,
        'varients_orders':varients_orders,
        'show_shopcart':True,
        'total_amount':total_amount,
        'total_products_in_cart':total_products_in_cart
    })
