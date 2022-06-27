from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from . import models
from django.template import RequestContext

# # Create your views here.

class Home(View):
    def get(self,response):
        return render(response,'index.html')


class Products(View):
    def get(self,response):
        produts=models.Products.objects.all()
        return render(response, 'products.html',{'Products':produts})

class SingleProduct(View):
    def get(self,response,pr):
        product = models.Products.objects.get(pk=pr)
        return render(response, 'single-product.html',{'Product':product})

class Contact(View):
     def get(self,response):
        return render(response, 'contact.html')

class About(View):
     def get(self,response):
        return render(response, 'about.html')

class Categorie(View):
    def get(self,response,cat):
        products=models.Categories.objects.get(name=cat).Products.all()
        return render(response,'categorie.html',{'Products':products,'categorie':cat})

class Cart(View):
    def get(self,response):
        return render(response,'cart.html')

def add(response,id):
    # v = RequestContext(response).get("app_config")
    # cart=v.get("Cart")
    # print(cart)
    return HttpResponse('card')