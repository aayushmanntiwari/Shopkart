from django.shortcuts import render,redirect
from django.http import *
from django.contrib.auth.models import User,Group
from django.contrib import messages
from .models import ExtendeRegisterUser

# Create your views here.
def validate(name=None,password=None,email=None,mobilenumber=None):
    if name!='' and password!='' and email!='' and mobilenumber!='':
        return True
    else:
        return False

def register(request):
    if request.method == 'POST':
        if validate(request.POST['fullname'],request.POST['password'],request.POST['email'],request.POST['mobilenumber']):
            try:
                user = User.objects.get(username = request.POST['email'])
                if user.groups.filter(name='user'):
                    messages.success(request,'User already exist,Please sign in !')
                    return redirect('/register/')
            except:
                name = request.POST['fullname'].split(' ')
                user = User.objects.create_user(username = request.POST['email'] ,password = request.POST['password'], first_name = name[0] ,last_name= name[1],email= request.POST['email'])
                mobilenumber = request.POST['mobilenumber']
                group = Group.objects.get(name='user')
                user.groups.add(group)
                extenderegisteruser = ExtendeRegisterUser(mobilenumber = mobilenumber , user = user)
                try:
                    extenderegisteruser.save()
                    messages.success(request,"User registered successfully,Please login In !")
                    return redirect('/login/')
                except:
                    messages.success(request,"Something went wrong ,Please register again !")
                    return redirect('/register/')
        else:
            messages.success(request,"Input can't be blank,Please try again !")
            return redirect('/register/')
    else:
        return render(request,'register.html')