from django.shortcuts import render,redirect
from django.http import *
from django.contrib.auth.models import User,Group
from django.contrib import auth
from django.contrib import messages
from django.db.models import F
from .models import Failed




# Create your views here.
def login(request):
    if request.method == 'POST':
        if request.POST['username']!='':
            #user =  auth.authenticate(username = request.POST['username'],password = request.POST['password'])
            #if user is not None:
            #    auth.login(request,user)
            #    return redirect('/')
            #else:
            #    messages.success(request,"Wrong username or password!")
            #    user = User.objects.get(username = request.POST['username'])
            #    print(user)
            #    try:
            #        counter = Failed.objects.get(user=user)
            #    except:
            #        counter = Failed.objects.create(user=user)
            #    print(counter)
            #    counter.count+=1
            #    counter.save()
            #    return render(request,'login.html',{'counter':counter})
            try:
                user = User.objects.get(username = request.POST['username'])
            except:
                user = False
            if user:
                #print(user.pk)
                return redirect('passwordvalidation',pk=user.pk ,num=0)
            else:
                messages.success(request,"Username not registered !")
                return render(request,'login.html')
        else:
            messages.success(request,"Username or password cannot be blank ,Try again !")
            return redirect('/login/')
    else:
        return render(request,'login.html')



def password(request,pk,num):
    user = User.objects.get(id = pk)
    #print(user.username)
    if request.method == 'POST':
        validate = auth.authenticate(username = user.username,password = request.POST['password'])
        if validate is not None:
            auth.login(request,validate)
            try:
                Counter = Failed.objects.get(user = user)
            except:
                Counter = Failed.objects.create(user = user)
            Counter.count = 0
            Counter.save()
            if user.groups.filter(name='user'):
                return redirect('/')
            if user.groups.filter(name='seller'):
                return redirect('/seller/home/')
        else:
            try:
                Counter = Failed.objects.get(user = user)
            except:
                Counter = Failed.objects.create(user = user)
            Counter.count+=1
            Counter.save()
            return redirect('passwordvalidation',pk=user.pk,num=Counter.count)
    else:
        if int(num) >=2:
            messages.success(request,"Try resetting the password !")
        return render(request,'login.html',{'showlogin':True,'showpassword':True})
   