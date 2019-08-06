from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Organization, Assessment
from ..register.models import User
# Create your views here.
def index(request):
	#Assessment.objects.all().delete()
	#Organization.objects.all().delete()
	try:
		user = User.objects.get(id = request.session['id'])
	except:
		return redirect(reverse('register:home'))
	context = {
		"user": user
	}
	try:
		name = request.session['company']
		company = Organization.objects.get(name = name)
		assessments = Assessment.objects.filter(user = user).filter(organization__name = company.name).order_by('-created_at')
		context["company"] = company
		
	except:
		assessments = Assessment.objects.filter(user = user).order_by('-created_at')
	context["assessments"] = assessments
	return render(request, 'assessment_history/index.html', context)

def company(request):
	try:
		user = User.objects.get(id = request.session['id'])
	except:
		return redirect(reverse('register:home'))
	request.session['company'] = request.POST['company']
	return redirect(reverse('assessment_history:home'))

def all(request):
	try:
		user = User.objects.get(id = request.session['id'])
	except:
		return redirect(reverse('register:home'))
	del request.session['company']
	return redirect(reverse('assessment_history:home'))
	
#def test(request):
#	try:
#		user = User.objects.get(id = request.session['id'])
#	except:
#		return redirect(reverse('register:home'))
#	company = request.POST['company']
#	#Organization.objects.create(name = company)
#	try:
#		organization = Organization.objects.get(name = company)
#	except:
#		Organization.objects.create(name = company)
#		organization = Organization.objects.get(name = company)
#	Assessment.objects.create(user = user, organization = organization)
#	return redirect(reverse('assessment_history:home'))