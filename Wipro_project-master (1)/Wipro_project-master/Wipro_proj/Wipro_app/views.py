from django.shortcuts import render, redirect
from django.urls import reverse

# Create your views here.
def login(request):
    return render(request, 'registration/login.html')
def AddOrg(request):
    return render(request, 'registration/AddOrg.html')
def MyHistory(request):
    return render(request, 'registration/MyHistory.html')
def ColleagueHistory(request):
    return render(request, 'registration/ColleagueHistory.html')
def home(request):
	#print("here")
	try:
		username = request.session['username']
		#print(username)
		#print("here")
	except:
		#print (e)
		#print("error")
		username = False
	if username:
		context = {
			"username": username
		}
		#print("success")
		return render(request, 'home.html', context)
	#print("render")
	else:
		return render(request, 'home.html')
def Assessment(request):
    return render(request, 'registration/Assessment.html')
def Profile(request):
    return render(request, 'registration/Profile.html')
def ForgetPassword(request):
    return render(request, 'registration/ForgetPassword.html')
def redirect(request):
	#print(reverse('home'))
	return home(request)