from django.shortcuts import render,redirect
from .models import Product,Varient,Image,Size,Color
from Category.models import Category
from django.db.models import Q
from django.http import *
from django.template.loader import render_to_string
from Orders.models import Orders
from django.contrib.auth.models import User,Group

# Create your views here.
def products(request,greatgrandparent_name=None,grandparent_name=None,parent_name=None,child_name=None):
    parent = Category.objects.all()
    childrenn = Category.objects.filter(level=1)
    subchildrenn = Category.objects.filter(level=2)
    subsubchildrenn = Category.objects.filter(level=3)
    

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
        orders = None
        total_products_in_cart = 0
        total_amount = 0
        varients_orders = None

    category = Category.objects.get(keywords = child_name)

    products = Product.objects.filter(category = category.id)

    images = Image.objects.all()

    sizes = Size.objects.all()

    colors = Color.objects.all()

    varients = []
    varients_sizes = []
    for product in products:
        varient = Varient.objects.filter(product_id = product.id).distinct('size')
        if len(varient)>=1:
            varients.append(varient[0])
            for id in varient.values_list('size',flat=True):
                if  (product.id,Size.objects.get(id = id).name) not in varients_sizes:
                    varients_sizes.append((product.id,Size.objects.get(id = id).name))
    return render(request,'index.html',{
        'showproducts':True,
        'shownavbar':True,
        'greatgrandparent_name':greatgrandparent_name,
        'grandparent_name':grandparent_name,
        'parent_name':parent_name,
        'child_name':child_name,
        'parent':parent,
        'childrenn':childrenn,
        'subchildrenn':subchildrenn,
        'subsubchildrenn':subsubchildrenn,
        'products':products,
        'varients':varients,
        'images':images,
        'sizes':sizes,
        'varients_sizes':varients_sizes,
        'orders':orders,
        'total_products_in_cart':total_products_in_cart,
        'total_amount':total_amount,
        'show_shopcart':show_shopcart,
        'varients_orders':varients_orders,
        'colors':colors
        })




def product(request,greatgrandparent_name=None,grandparent_name=None,parent_name=None,child_name=None,product_name=None):
    parent = Category.objects.all()
    childrenn = Category.objects.filter(level=1)
    subchildrenn = Category.objects.filter(level=2)
    subsubchildrenn = Category.objects.filter(level=3)

    curr_product = Product.objects.get(id = request.POST.get('product_id'))

    images = Image.objects.all()

    sizes = Size.objects.all()

    colors = Color.objects.all()

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
        orders = None
        total_products_in_cart = 0
        total_amount = 0
        varients_orders = None

    if curr_product.varient == "Size":
        curr_varient = Varient.objects.get(Q(product_id = request.POST.get('product_id')) and Q(size_id = request.POST.get('varient_size_id')))
        #print(curr_varient)
        all_varients = Varient.objects.filter(product_id = request.POST.get('product_id')).distinct('size_id')
        curr_varient_colors = None

    else:
        curr_varient = Varient.objects.get(Q(product_id = request.POST.get('product_id')) & Q(id = request.POST.get('varient_id')) & Q(size_id =  request.POST.get('varient_size_id')))
        
        #print("curr_varient: ",curr_varient)
        
        curr_varient_colors = Varient.objects.filter(Q(product_id =  request.POST.get('product_id')) & Q(size_id = request.POST.get('varient_size_id')))
        
        #print("curr_varient_colors: ",curr_varient_colors)


        all_varients = Varient.objects.filter(product_id = request.POST.get('product_id')).distinct('size_id')


        #print("all_varients: ",all_varients)


        images = Image.objects.all()

        sizes = Size.objects.all()
    
    if request.POST.get('quantity') is not None:
        Orders.objects.get_or_create(product = curr_product,varient = curr_varient,user = request.user ,quantity = request.POST.get('quantity'))
    return render(request,'index.html',{
            'showproductspage':True,
            'shownavbar':True,
            'parent':parent,
            'childrenn':childrenn,
            'subchildrenn':subchildrenn,
            'subsubchildrenn':subsubchildrenn,
            'greatgrandparent_name':greatgrandparent_name,
            'grandparent_name':grandparent_name,
            'parent_name':parent_name,
            'child_name':child_name,
            'product_name':product_name,
            'all_varients':all_varients,
            'sizes':sizes,
            'product_id':request.POST.get('product_id'),
            'curr_varient':curr_varient,
            'curr_product':curr_product,
            'curr_varient_colors':curr_varient_colors,
            'images':images,
            'orders':orders,
            'total_products_in_cart':total_products_in_cart,
            'total_amount':total_amount,
            'show_shopcart':show_shopcart,
            'varients_orders':varients_orders,
            'colors':colors
    })



def color_options_based_on_size(request):
    data = {}
    if request.method == 'POST':
        #print(request.POST.get('product_id'))
        #print(request.POST.get('varient_size_id'))
        curr_varient = Product.objects.get(id = request.POST.get('product_id'))
        child = Category.objects.get(id = curr_varient.category_id)
        parent = Category.objects.get(id = child.parent_id)
        grandparent = Category.objects.get(id = parent.parent_id)
        greatgrandparent = Category.objects.get(id = grandparent.parent_id)
        images = Image.objects.all()
        curr_varient_colors = Varient.objects.filter(Q(product_id =  request.POST.get('product_id')) & Q(size_id = request.POST.get('varient_size_id')))
       
        context = {
            'images':images,
            'greatgrandparent_name':greatgrandparent.title,
            'grandparent_name':grandparent.title,
            'parent_name':parent.title,
            'child_name':child.title,
            'curr_varient_colors':curr_varient_colors,
            'curr_varient':curr_varient,
        }
        data = {'rendered_table': render_to_string('products-colors.html',context=context)}
    return JsonResponse(data)