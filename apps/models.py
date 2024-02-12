from django.db import models
from django.db.models import Model, CharField, ImageField


# Create your models here.


# class Ads():
#     title = models.CharField(max_length=255)
#     ad_source = models.CharField(max_length=255) #Aslida Foreign Key bo'llishi kerak.
#     image = models.ImageField(upload_to='media/ads', default='media/default.jpg')

class Ads(Model):
    title = CharField(max_length=255)
    ad_source = CharField(max_length=255)
    image = ImageField(upload_to='media/ads', default='media/default.jpg')