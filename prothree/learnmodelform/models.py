from django.db import models

# Create your models here.

GENDER_CHOICES = (
	('M','Male'),
	('F','Female'),
	('O','Others'),
)
RELIGION_CHOICES = (
	('ISM','Islam'),
	('HIN','Hindu'),
	('OTH','Others'),
)

class User(models.Model):
	formalName = models.CharField(max_length=250)
	nickName = models.CharField(max_length=250)
	contactNumber = models.CharField(max_length=20,unique=True)
	dateOfBirth = models.DateField(null=True)
	gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
	religion = models.CharField(max_length=10,choices=RELIGION_CHOICES)
	email = models.EmailField()
	password = models.CharField(max_length=250)