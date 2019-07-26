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
	if Permission.objects.filter(desc='employee') and Permission.objects.filter(desc='supervisor').exists() :
		print('Employee && supervisor permission already present')
	else:
		# permissions hard coded as of now
		print('Creating permissions')
		Permission.objects.create(desc='employee')
		Permission.objects.create(desc='supervisor')
	try:
		username = request.session['username']
	except:
		username = False
	context = {
		"permissions":Permission.objects.all()
	}
	if username:
		context["username"] = username
	return render(request, 'register/index.html', context)
		
def loginindex(request):
	#todo: admin verification to access page
	#try:
	#	user = User.objects.get(id = request.session['id'])
	#	permission = Permission.objects.get(id = "admin id goes here")
	#	user.permissions.get(id = permission.id)
	#except:
	#	return redirect(reverse('login:home'))
	if Permission.objects.filter(desc='employee').exists() and Permission.objects.filter(desc='supervisor').exists() :
		print('Employee && supervisor permission already present')
	else:
		# permissions hard coded as of now
		print('Creating permissions')
		Permission.objects.create(desc='employee')
		Permission.objects.create(desc='supervisor')
	try:
		username = request.session['username']
	except:
		username = False
	context = {
		"permissions":Permission.objects.all()
	}
	if username:
		context["username"] = username
	return render(request, 'register/login.html', context)

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

    #permissions hard coded as of now
    # Permission.objects.create(desc='employee')
    # Permission.objects.create(desc='supervisor')

    # User.objects.create(username = request.POST['username'], email = request.POST['email'], pwhash = pwhash)
    # request.session['username'] = request.POST['username']
    # request.session['permissions']=request.POST['permissions']
    #
    # namer = User.objects.get(email = request.POST['email'])

    # User.objects.all().delete()
    if Permission.objects.filter(desc='employee').exists() and Permission.objects.filter(desc='supervisor').exists() :
        print('Employee && supervisor permission already present')
    else:
        # permissions hard coded as of now
        print('Creating permissions')
        Permission.objects.create(desc='employee')
        Permission.objects.create(desc='supervisor')



    # user=User.objects.all()
    #
    # for ss in user:
    #     for permission in ss.permissions.all():
    #         print(' the user is '+ ss.username+" "+ ss.email+ " " +permission.desc)

    #
    #
    User.objects.create(username = request.POST['username'], email = request.POST['email'], pwhash = pwhash)

    user=User.objects.get(username=request.POST['username'],email=request.POST['email'],pwhash=pwhash)

    permission=Permission.objects.get(desc=request.POST['permissions'])

    user.permissions.add(permission)

    user.save()
    permission.save()

    users=User.objects.all()

    # for ss in user:
    #     print(ss.username)

    for ss in users:
        for permission in ss.permissions.all():
            print('The user entered is having the following '+ss.username+" "+ss.email+" "+permission.desc)


    request.session['id']   =  user.id
    request.session['username'] = request.POST['username']
    request.session['permissions'] = request.POST['permissions']

    # request.session['username'] = request.POST['username']
    # request.session['permissions']=Permission.objects.get(desc='employee')


    # namer.permissions.add(Permission.objects.get(desc='employee'))
    # namer.save()

    # Permission.objects.all().delete()
    # permissions=Permission.objects.all()

    # # ppall=User.objects.all()
    #
    # for ss in permissions:
    #     print('the user permission stored is '+ss.desc)
    # #
    # for pp in namer:
    #     print('the namer is'+pp.permissions)
    #
    # request.session['id'] = namer.id
    # request.session['username'] = namer.username
    #
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
    return redirect(reverse('home'))
    
def logout(request):
	del request.session['username']
	del request.session['id']
	return redirect(reverse('home'))

# Create your views here.
