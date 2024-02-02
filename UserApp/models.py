from django.db import models
from django.db.models.deletion import CASCADE
from AdminApp.models import *

# Create your models here.
class Login(models.Model):
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=30)
    email=models.EmailField()
    phone=models.CharField(max_length=20)
class Contact(models.Model):
    name=models.CharField(max_length=20)  
    email=models.EmailField(max_length=25) 
    subject=models.CharField(max_length=40)
    message=models.CharField(max_length=2000)
class Cart(models.Model):
    userid=models.ForeignKey(Login,on_delete=CASCADE) 
    productid=models.ForeignKey(AddMov,on_delete=CASCADE) 
    quantity=models.IntegerField()
    total=models.IntegerField()
    status=models.IntegerField(default=0) 
class Checkout(models.Model):
    userid=models.ForeignKey(Login,on_delete=CASCADE)
    cartid=models.ForeignKey(Cart,on_delete=CASCADE,null=True)  
    address=models.CharField(max_length=255)  
    city=models.CharField(max_length=25)
    state=models.CharField(max_length=15,default="")
    country=models.CharField(max_length=25)
    zip=models.CharField(max_length=15)
     