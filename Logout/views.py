from django.shortcuts import render,redirect
from django.http import *
from django.contrib import auth
from django.contrib.auth.models import User,Group

# Create your views here.
def logout(request):
    user = User.objects.get(username = request.user)
    if user.groups.filter(name='user'):
        auth.logout(request)
        return redirect('/')
    else:
        return redirect('/login/')