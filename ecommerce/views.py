from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

# # Create your views here.

class Home(View):
    def get(self,response):
        return render(response,'index.html')


class Products(View):
    def get(self,response):
        return render(response, 'products.html')

class SingleProduct(View):
    def get(self,response)
        return render(response, 'single-product.html')

class Contact(View):
     def get(self,response):
        return render(request, 'contact.html')

class About(View):
     def get(self,response)
        return render(request, 'about.html')

class Categorie(View):
    def get(self,response,cat):
        title = {
            "men": "Men\'s",
            "women": "Women's",
            "kid": "Kid's",
            "accessories": "Accessories",
        }
        return render(response,'categorie.html',{'categorie':cat,'title':title[cat]})