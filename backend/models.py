from django.db import models

# Create your models here.

class admin_db(models.Model):
    username=models.CharField(max_length=100,null=True,blank=True)
    email=models.EmailField(max_length=100,null=True,blank=True)
    password=models.CharField(max_length=100,null=True,blank=True)
    r_password=models.CharField(max_length=100,null=True,blank=True)
    mobile=models.IntegerField(null=True,blank=True)

class cat_db(models.Model):
    category=models.CharField(max_length=100,null=True,blank=True)
    quality=models.CharField(max_length=100,null=True,blank=True)
    image=models.ImageField(upload_to="cat_profile",null=True,blank=True)

class item_db(models.Model):
    name=models.CharField(max_length=100,null=True,blank=True)
    price=models.IntegerField(null=True,blank=True)
    category=models.CharField(max_length=100,null=True,blank=True)
    size=models.CharField(max_length=100,null=True,blank=True)
    image=models.ImageField(upload_to="item_profile",null=True,blank=True)

class contact_db(models.Model):
    name=models.CharField(max_length=100,null=True,blank=True)
    number=models.IntegerField(null=True,blank=True)
    email=models.EmailField(max_length=100,null=True,blank=True)
    need=models.CharField(max_length=100,null=True,blank=True)
    message=models.CharField(max_length=500,null=True,blank=True)
