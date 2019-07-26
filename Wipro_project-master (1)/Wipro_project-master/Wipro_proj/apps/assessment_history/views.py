from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Organization, Assessment
from ..register.models import User
# Create your views here.
def index(request):