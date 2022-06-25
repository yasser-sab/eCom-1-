from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from . import models

# # Create your views here.

class Home(View):
    def get(self,response):
        categories=models.Categories.objects.all()
        return render(response,'index.html',{"Categories":categories})


class Products(View):
    def get(self,response):
        produts=models.Products.objects.all()
        categories=models.Categories.objects.all()
        return render(response, 'products.html',{'Products':produts,"Categories":categories})

class SingleProduct(View):
    def get(self,response,pr):
        product = models.Products.objects.get(pk=pr)
        categories=models.Categories.objects.all()
        return render(response, 'single-product.html',{'Product':product,"Categories":categories})

class Contact(View):
     def get(self,response):
        return render(response, 'contact.html')

class About(View):
     def get(self,response):
        return render(response, 'about.html')

class Categorie(View):
    def get(self,response,cat):
        products=models.Categories.objects.get(name=cat).Products.all()
        categories=models.Categories.objects.all()
        # title = {
        #     "men": "Men\'s",
        #     "women": "Women's",
        #     "kid": "Kid's",
        #     "accessories": "Accessories",
        # }
        return render(response,'categorie.html',{'Products':products,'categorie':cat,"Categories":categories})