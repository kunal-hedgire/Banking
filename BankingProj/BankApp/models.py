from django.db import models


# Create your models here.
class Register(models.Model):
    customerName=models.CharField(max_length=30)
    password=models.CharField(max_length=25)
    customerAge=models.PositiveSmallIntegerField()
    #imgpath = models.ImageField()

class Login(models.Model):
    userName=models.CharField(max_length=25)
    password=models.CharField(max_length=10)
