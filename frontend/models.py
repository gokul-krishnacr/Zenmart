from django.db import models

# Create your models here.
class reg_db1(models.Model):
    name=models.CharField(max_length=100,null=True,blank=True)
    email=models.EmailField(max_length=100,null=True,blank=True)
    password=models.CharField(max_length=100,null=True,blank=True)
    r_password=models.CharField(max_length=100,null=True,blank=True)
    mobile=models.IntegerField(null=True,blank=True)