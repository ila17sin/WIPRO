from django.db import models

# Create your models here.

class Org(models.Model):
    OrgID = models.CharField(max_length = 120)
    OrgName = models.CharField(max_length = 120)
    OrgLocation = models.CharField(max_length = 120)
    OrgSize = models.CharField(max_length = 120)
    OrgDomain = models.CharField(max_length = 120)

class Assessment(models.Model):
    AssessmentID = models.CharField(max_length = 120)
    OrgID = models.CharField(max_length = 120)
    userID = models.CharField(max_length = 300)
    timestamp = models.DateTimeField(max_length = 500)

class Category(models.Model):
    CategoryID = models.CharField(max_length = 120)
    Categorydesc = models.CharField(max_length = 120)

class Question(models.Model):
    QuestionID = models.CharField(max_length = 120)
    QuestionDesc= models.CharField(max_length = 120)
    CategoryID = models.CharField(max_length=120)

class QuestionList(models.Model):
    QuestionID = models.CharField(max_length = 120)
    AssessmentID= models.CharField(max_length = 120)
    Rating = models.CharField(max_length=120)

class userdetails(models.Model):
    username = models.CharField(max_length = 120)
    supervisorID = models.CharField(max_length=120)
    permissionID = models.CharField(max_length=120)