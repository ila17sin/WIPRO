from __future__ import unicode_literals
from django.db import models
from ..register.models import User

# Create your models here.
class Organization(models.Model):
	name = models.CharField(max_length = 255)
	created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class Assessment(models.Model):
	#this is how to make a one-to-many field.  Assessments will have one user, while users will have many assessments.
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)