from django.db import models

# Create your models here.
from django.db.models import CASCADE


class ClientRegister_Model(models.Model):
    username = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=10)
    phoneno = models.CharField(max_length=10)
    country = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    gender= models.CharField(max_length=30)
    address= models.CharField(max_length=30)


class predict_cybersecure_smart_city(models.Model):

    RID= models.CharField(max_length=300)
    city= models.CharField(max_length=300)
    city_ascii= models.CharField(max_length=300)
    lat= models.CharField(max_length=300)
    lng= models.CharField(max_length=300)
    country= models.CharField(max_length=300)
    iso2= models.CharField(max_length=300)
    iso3= models.CharField(max_length=300)
    admin_name= models.CharField(max_length=300)
    capital= models.CharField(max_length=300)
    population= models.CharField(max_length=300)
    optimization_block= models.CharField(max_length=300)
    features_block= models.CharField(max_length=300)
    Prediction= models.CharField(max_length=300)


class detection_accuracy(models.Model):

    names = models.CharField(max_length=300)
    ratio = models.CharField(max_length=300)

class detection_ratio(models.Model):

    names = models.CharField(max_length=300)
    ratio = models.CharField(max_length=300)



