from django.shortcuts import render,redirect
from django.http import *
from django.db.models import Q
from .models import Orders
from Category.models import Category
from django.contrib.auth.models import User,Group
from .models import Orders
from Products.models import Varient,Image,Size,Product,Color
import json

# Create your views here.
def showcart(request):
    try:
        user = User.objects.get(username = request.user)
        orders = Orders.objects.filter(user_id  = user.id)
        Orders.objects.filter(quantity = 0).delete()
        varients_orders = Varient.objects.all()
        print(orders)
        if len(orders)!=0:
            total_products_in_cart = len(orders)
        else:
            total_products_in_cart = 0
            orders = None
            varients_orders = None
        if len(orders)!=0:
            total_amount = sum([int(val.amount) for val in orders])
            if total_amount <=500:
                delivery_charge = True
                total_amount+=len(orders)*50
            else:
                delivery_charge = False
        else:
            total_amount = 0
            orders = None
            varients_orders = None
            delivery_charge = False
        show_shopcart = True
    except:
        show_shopcart = False
        orders = None
        total_amount = 0
        total_products_in_cart = 0
        varients_orders = None
        delivery_charge = False
    parent = Category.objects.all()
    childrenn = Category.objects.filter(level=1)
    subchildrenn = Category.objects.filter(level=2)
    subsubchildrenn = Category.objects.filter(level=3)
    images = Image.objects.all()
    sizes = Size.objects.all()
    varients = Varient.objects.all()
    colors = Color.objects.all()
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
        'total_products_in_cart':total_products_in_cart,
        'colors':colors,
        'show_shopcart':show_shopcart,
        'delivery_charge':delivery_charge,
    })




def updateItem(request):
    data = json.loads(request.body)
    varient_id = data['varient_id']
    action = data['action']
    user_check = data['user_check']
    quantity = data['quantity'] or None
    product_id = data['product_id']
    varient = Varient.objects.get(id = varient_id)
    product = Product.objects.get(id = product_id)
    '''print('varient_id:',varient_id)
    print("action: ",action)
    print("user_check: ",user_check)
    print("quantity: ",quantity)
    print("product_id: ",product_id)
    print("varient: ",varient)
    print('product: ',product)'''
    if action == "add":
        orders,created = Orders.objects.get_or_create(product = product,varient = varient,user = request.user)
        if created:
            orders.quantity+=int(quantity)
            orders.save()
        else:
            orders.quantity+=int(quantity)
            orders.save()
    elif action == "removing":
        orders = Orders.objects.get(varient_id = varient_id)
        if orders.quantity > 0:   
           orders.quantity = (orders.quantity - 1)
           orders.save()
        else:
            orders.delete()
    elif action == "adding":
        orders = Orders.objects.get(varient_id = varient_id)
        if orders.quantity>=0:
           orders.quantity = (orders.quantity + 1)
           orders.save()
    return JsonResponse('Item added sucessfully !',safe=False)



def deleteorderitem(request):
    data = json.loads(request.body)
    order_id = data['order_id']
    Orders.objects.get(id = order_id).delete()
    return JsonResponse('Item delted sucessfully !',safe=False)