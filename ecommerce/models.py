from django.db import models
from django.contrib.auth.models import User
# Create your models here.





class Products(models.Model):
    name = models.CharField('Product_Name', max_length=128)
    price = models.FloatField('Product_Price' ,default=0.0)
    stock = models.IntegerField('Product_Stock' ,default=0)
    promotion = models.CharField('Product_Promotion' ,max_length=180)
    description = models.TextField('Product_description' ,blank=True)
    thumbnail = models.ImageField('Prodact_image' ,upload_to="products", blank=True, null=True)
    options = models.CharField('Product_options' ,max_length=120)

    def __str__(self):
        return self.name

class Tags(models.Model):
    libelle = models.CharField('lib_TAG', max_length=120)
    Product = models.ForeignKey(Products ,null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Client(models.Model):
    name = models.CharField('Client', max_length=120)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name




class Categories(models.Model):
    name = models.CharField('Name', default=128, max_length=128)
    description = models.TextField('description', blank=True)
    Products = models.ManyToManyField(Products)


    def __str__(self):
        return self.name



class Commande(models.Model):
    date = models.DateTimeField('date')
    quant = models.IntegerField('quantite', default=0)
    Client = models.ForeignKey(Client, blank=True, null=True, on_delete=models.CASCADE)
    etat = models.CharField('etat', max_length=120)
    Product = models.ManyToManyField(Products)


    def __str__(self):
        return self.etat















