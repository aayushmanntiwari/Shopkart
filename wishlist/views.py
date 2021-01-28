from django.shortcuts import render,redirect
from django.contrib.auth.models import User,Group
from django.http import *
import json
from Products.models import Varient,Image,Size,Color,Product
from Orders.models import Orders
from Category.models import Category
from .models import Wishlist

# Create your views here.
def showwishlist(request):
    parent = Category.objects.all()
    childrenn = Category.objects.filter(level=1)
    subchildrenn = Category.objects.filter(level=2)
    subsubchildrenn = Category.objects.filter(level=3)
    images = Image.objects.all()
    sizes = Size.objects.all()
    colors = Color.objects.all()
    varients = Varient.objects.all()
    try:
        wishlist = Wishlist.objects.filter(user_id = request.user.id)
    except:
        wishlist = None
    try:
        user = User.objects.get(username = request.user)
        orders = Orders.objects.filter(user_id  = user.id)
        print(orders)
        varients_orders = Varient.objects.all()
        if len(orders)!=0:
            total_products_in_cart = len(orders)
        else:
            total_products_in_cart = 0
            orders = None
        if len(orders)!=0:
            total_amount = sum([int(val.amount) for val in orders])
        else:
            total_amount = 0
            orders = None
        show_shopcart = True
    except:
        show_shopcart = False
        total_amount = 0
        total_products_in_cart = 0
        orders = None
        varients_orders = None
    return render(request,'index.html',{
        'showwishlist':True,
        'shownavbar':True,
        'show_shopcart':show_shopcart,
        'parent':parent,
        'childrenn':childrenn,
        'subchildrenn':subchildrenn,
        'subsubchildrenn':subsubchildrenn,
        'images':images,
        'sizes':sizes,
        'colors':colors,
        'wishlist':wishlist,
        'varients':varients,
        'orders':orders,
        'varients_orders':varients_orders,
        'total_products_in_cart':total_products_in_cart,
        'total_amount':total_amount,
        
    })



def addtowishlist(request):
    data = json.loads(request.body)
    varient_id = data['varient_id']
    product_id = data['product_id']
    user_check = data['user_check']
    action = data['action']
    varient = Varient.objects.get(id = varient_id)
    product = Product.objects.get(id = product_id)
    if action == "addtolist" and user_check == 'True':
        Wishlist.objects.get_or_create(varient = varient ,product = product,user = request.user)
    return JsonResponse('Item added to wishlist sucessfully !',safe=False)


def deletewishitem(request):
    data = json.loads(request.body)
    order_id = data['order_id']
    Wishlist.objects.get(id = order_id).delete()
    return JsonResponse('wish list Item deleted sucessfully !',safe=False)

    