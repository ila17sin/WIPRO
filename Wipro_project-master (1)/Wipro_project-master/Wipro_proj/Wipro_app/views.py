from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
def login(request):
    return render(request, 'registration/login.html')
def AddOrg(request):
    return render(request, 'registration/AddOrg.html')
def MyHistory(request):
    return render(request, 'registration/MyHistory.html')
def ColleagueHistory(request):
    return render(request, 'registration/ColleagueHistory.html')
def home(request):
    return render(request, 'home.html')
def Assessment(request):
    return render(request, 'registration/Assessment.html')
def Profile(request):
    return render(request, 'registration/Profile.html')
def ForgetPassword(request):
    return render(request, 'registration/ForgetPassword.html')