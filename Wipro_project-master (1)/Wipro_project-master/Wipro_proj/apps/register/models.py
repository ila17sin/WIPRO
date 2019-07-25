
from __future__ import unicode_literals

from django.db import models
import bcrypt

import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@wipro.com')

# Create your models here.
class RegistrationManager(models.Manager):
    def regvalidator(self, username, email):
        errors = []
        if len(username) < 1:
            errors.append("username cannot be blank")
        if not EMAIL_REGEX.match(email):
            errors.append("must enter a valid WIPRO email")
        users = User.objects.all()
        for user in users:
        	if user.username == username:
        		errors.append("username already in use")
        	if user.email == email:
        		errors.append("email already in use")
        return {'errors': errors}
    def bcryptor(self, password):
        hashword = bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt())
        return {'pwhash': hashword.decode('utf8')}
    def logvalidator(self, email, password):
        errors = []
        try:
            user = self.get(email = email)
            if bcrypt.checkpw(password.encode('utf8'), user.pwhash.encode('utf8')):
                return {'user': user, 'errors': errors}
            errors.append("Incorrect password")
        except Exception:
        	errors.append("unrecognized email address")
        return {'errors': errors}


class Permission(models.Model):
	desc = models.CharField(max_length = 255)

class User(models.Model):
    username = models.CharField(max_length = 255)
    email = models.EmailField()
    pwhash = models.CharField(max_length = 255)
    permissions = models.ManyToManyField(Permission)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = RegistrationManager()
    
	