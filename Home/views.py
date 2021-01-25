from django.shortcuts import render,redirect
from django.http import *
from Category.models import Category
from django.db.models import Q
from mptt.fields import TreeNodeChoiceField
from django.contrib.auth.models import User,Group
from django.contrib import auth
from django.contrib import messages
from Orders.models import Orders
from Products.models import Varient,Image,Size

# Create your views here.
def home(request):
    parent = Category.objects.all()
    childrenn = Category.objects.filter(level=1)
    subchildrenn = Category.objects.filter(level=2)
    subsubchildrenn = Category.objects.filter(level=3)

    print(parent)
    print(childrenn)
    print(subchildrenn)
    print(subsubchildrenn)
    if request.user.is_authenticated:
        user = User.objects.get(username = request.user)
        if user.groups.filter(name='user'):
            try:
                print(1)
                orders = Orders.objects.filter(user_id  = user.id)
                varients_orders = Varient.objects.all()
                images = Image.objects.all()
                sizes = Size.objects.all()
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
                return render(request,'index.html',{'showhome':True,'parent':parent,'childrenn':childrenn,'subchildrenn':subchildrenn,'shownavbar':True,'orders':orders,'total_products_in_cart':total_products_in_cart,'total_amount':total_amount,'show_shopcart':show_shopcart,'subsubchildrenn':subsubchildrenn,'varients_orders':varients_orders,'images':images,'sizes':sizes})
            except:
                print(2)
                show_shopcart = False
                total_amount = 0
                total_products_in_cart = 0
                return render(request,'index.html',{'showhome':True,'parent':parent,'childrenn':childrenn,'subchildrenn':subchildrenn,'shownavbar':True,'subsubchildrenn':subsubchildrenn,'show_shopcart':show_shopcart,'total_products_in_cart':total_products_in_cart,'total_amount':total_amount})
        else:
            messages.success(request,"You are not authorized to do this")
            return redirect('/login/')
            
    else:
        total_amount = 0
        total_products_in_cart = 0
        show_shopcart = False
        return render(request,'index.html',{'showhome':True,'parent':parent,'childrenn':childrenn,'subchildrenn':subchildrenn,'shownavbar':True,'total_products_in_cart':total_products_in_cart,'total_amount':total_amount,'show_shopcart':show_shopcart,'subsubchildrenn':subsubchildrenn,'show_shopcart':show_shopcart})