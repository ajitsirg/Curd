from django.db import models

# Create your models here.


class Coustmer(models.Model):
    name      = models.CharField(max_length=30,blank=True,null=True)
    age       = models.DateField(auto_now=False, auto_now_add=False,blank=True,null=True)
    phone     = models.IntegerField(max_length=11,unique=True)
    email     = models.EmailField(null=True, blank=True)
    
    address   = models.TextField(max_length=255,blank=True,null=True)
    city      = models.CharField(max_length=35,blank=True,null=True)
    state     = models.CharField(max_length=40,blank=True,null=True)
    country   = models.CharField(max_length=30 ,blank=True,null=True)
    
    def __str__(self):
        return str(self.name) 
    
    
class Vendor(models.Model):
    name      = models.CharField(max_length=30,blank=True,null=True)
    age       = models.DateField(auto_now=False, auto_now_add=False,blank=True,null=True)
    phone     = models.IntegerField(max_length=11,unique=True)
    email     = models.EmailField(null=True, blank=True)
    companyName= models.CharField(max_length=100,blank=True,null=True)
    gstNumber = models.CharField(max_length=100, blank=True, null=True)
    panCard   = models.CharField(max_length=10, blank=True, null=True)
    panImage  = models.ImageField(upload_to='images/', blank=True, null=True )
    address   = models.TextField(max_length=255,blank=True,null=True)
    city      = models.CharField(max_length=35,blank=True,null=True)
    state     = models.CharField(max_length=40,blank=True,null=True)
    country   = models.CharField(max_length=30 ,blank=True,null=True)
    
    def __str__(self):
        return str(self.name)    