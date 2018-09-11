from django.db import models

# Create your models here.

class userInfo(models.Model):
	firstName = models.CharField(max_length=264)
	lastName = models.CharField(max_length=264)
	email = models.EmailField(max_length=70)

	# def __str__(self):
	# 	return self.firstName,self.lastName,self.email