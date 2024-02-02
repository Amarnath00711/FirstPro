from django.db import models

# Create your models here.
class AddCat(models.Model):
    catname=models.CharField(max_length=20)
    catdescription=models.CharField(max_length=100)
    
    images=models.ImageField(upload_to='photoos',default='null.jpg')


class AddMov(models.Model):
    moviename=models.CharField(max_length=20)
    moviecategory=models.CharField(max_length=20)
    movielang=models.CharField(max_length=20)
    moviegenre=models.CharField(max_length=20)
    price=models.IntegerField(default=0)
    image=models.ImageField(upload_to='photos',default='null.jpg')