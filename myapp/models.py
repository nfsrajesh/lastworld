from django.db import models
from django_countries.data import COUNTRIES
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User
# from phonenumber_field.widgets import PhoneNumberPrefixWidget

# Create your models here.

class userprofile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True,unique=True)
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=30)
    email=models.EmailField()
    phonenumber=PhoneNumberField()
    country = models.CharField(choices=sorted(COUNTRIES.items()),max_length=50)
    password=models.CharField(max_length=100)


    def __str__(self):
         return f"{self.firstname},{self.lastname}"
