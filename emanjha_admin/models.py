from django.db import models

# Create your models here.
class Facilities(models.Model):
    name=models.CharField(max_length=200)
    history=models.CharField(max_length=2000, default="empty")
    image=models.FileField(upload_to='facilities',default="")

class Activities(models.Model):
    name=models.CharField(max_length=200)
    history=models.CharField(max_length=2000, default="empty")
    image=models.FileField(upload_to='activities',default="")

class Categories(models.Model):
    name=models.CharField(max_length=500)
    history=models.CharField(max_length=2000, default="empty")
    image=models.FileField(upload_to='categories',default="")

class Api_document(models.Model):
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=300)
    api_url = models.CharField(max_length=200)

class Location_add(models.Model):
    name = models.CharField(max_length=300)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=50)
    address = models.CharField(max_length=400)
    logitude = models.CharField(max_length=50)
    latitude = models.CharField(max_length=50)
    overview = models.CharField(max_length=1000)
    category = models.CharField(max_length=2000)
    facility = models.CharField(max_length=2000)
    activity = models.CharField(max_length=2000)
    thumbnail1=models.FileField(upload_to='thumbnail1',default="")
    thumbnail2=models.FileField(upload_to='thumbnail2',default="")
    thumbnail3=models.FileField(upload_to='thumbnail3',default="")
    other1=models.FileField(upload_to='other1',default="")
    other2=models.FileField(upload_to='other2',default="")
    other3=models.FileField(upload_to='other3',default="")
