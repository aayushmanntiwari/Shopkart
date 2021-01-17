from django.shortcuts import render,redirect
from django.http import *
from django.contrib.auth.models import User,Group
from django.contrib import messages
from .models import Seller
from Category.models import Category

# Create your views here.
def sellerhomepage(request):
    category = Category.objects.filter(level = 2)
    if request.method == 'POST':
        id = request.POST['category']
        subchild = Category.objects.get(id = id)
        '''Every time when you add new child make sure to add here in this condition has well '''
        child = Category.objects.get(id = subchild.parent_id)
        '''Here we are validating for every subchild in which child they belong to and make do the same check for all child '''
        if str(child.title).replace(' ','').lower() == 'topwear':
            return render(request,'seller-home.html',{'show_add_product_button':True,'childname':str(child.title).replace(' ','').lower(),'child_id':child.id,'subchild_id':id,'category':category})
    else:
        return render(request,'seller-home.html',{'category':category,'show_add_product_button':False})


def validate(firstname=None,lastname=None,email=None,mobilenumber=None,password=None):
    if firstname!="" and email!="" and mobilenumber!="" and password!="":
        return True
    else:
        return False

def seller_register(request):
    if request.method == 'POST':
        if validate(firstname= request.POST['firstname'],lastname=request.POST['lastname'],email= request.POST['email'] ,mobilenumber= request.POST['mobilenumber'],password= request.POST['password']):
            try:
                user = User.objects.get(username=request.POST['email'])
                if user.groups.filter(name='seller'):
                    messages.success(request,"Seller already exist!")
                    return redirect('/seller/register/')
                else:
                    messages.success(request,"Something is misssing !")
                    return redirect('/seller/register/')
            except:
                user = User.objects.create_user(username=request.POST['email'],password= request.POST['password'],first_name=request.POST['firstname'],last_name=request.POST['lastname'],email= request.POST['email'])
                mobilenumber = request.POST['mobilenumber']
                firstname = request.POST['firstname']
                lastname = request.POST['lastname']
                group = Group.objects.get(name='seller')
                user.groups.add(group)
                sellerextended = Seller(mobilenumber = mobilenumber,firstname = firstname ,lastname = lastname,seller = user)
                try:
                    sellerextended.save()
                    messages.success(request,"Registered Successfully,Happy selling !")
                    return redirect('/seller/register/')
                except:
                    messages.success(request,"Something Went wrong ,Contact us !")
                    return redirect('/seller/register/')
        else:       
            messages.success(request,"Field can not be blank!")
            return redirect('/seller/register/')
    else:
        return render(request,'seller-register.html')


