# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from .models import User, Permission
import random
import string

from django.shortcuts import render

def index(request):
	#todo: admin verification to access page
	#try:
	#	user = User.objects.get(id = request.session['id'])
	#	permission = Permission.objects.get(id = "admin id goes here")
	#	user.permissions.get(id = permission.id)
	#except:
	#	return redirect(reverse('login:home'))
	try:
		username = request.session['username']
	except:
		username = False
	if username:
		context = {
			"username": username
		}
		return render(request, 'register/index.html', context)
	else:
		return render(request, 'register/index.html')
    
def register(request):
    user = User.objects.regvalidator(request.POST['username'], request.POST['email'])
    if user['errors'] != []:
        for errors in user['errors']:
            messages.add_message(request, messages.ERROR, errors)
        return redirect(reverse('register:home'))
    password = ""
    for i in range(8):
    	password += random.choice(string.ascii_letters + string.digits);
    prehash = User.objects.bcryptor(password)
    pwhash = prehash['pwhash']
    User.objects.create(username = request.POST['username'], email = request.POST['email'], pwhash = pwhash)
    request.session['username'] = request.POST['username']
    namer = User.objects.get(email = request.POST['email'])
    request.session['id'] = namer.id
    request.session['username'] = namer.username 
    messages.add_message(request, messages.INFO, password)
    return redirect(reverse('register:home'))
    
def login(request):
    user = User.objects.logvalidator(request.POST['email'], request.POST['password'])
    if user['errors'] != []:
        for errors in user['errors']:
            messages.add_message(request, messages.ERROR, errors)
        return redirect(reverse('register:home'))
    namer = User.objects.get(email = request.POST['email'])
    request.session['id'] = namer.id
    request.session['username'] = namer.username
    return redirect(reverse('register:home'))
    
def logout(request):
	del request.session['username']
	del request.session['id']
	return redirect(reverse('register:home'))

# Create your views here.
