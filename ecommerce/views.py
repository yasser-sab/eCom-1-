from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

# # Create your views here.

class Home(View):
    def get(self,response):
        return render(response,'index.html')

class Categorie(View):
    def get(self,response,cat):
        title = {
            "men": "Men\'s",
            "women": "Women's",
            "kid": "Kid's",
            "accessories": "Accessories",
        }
        return render(response,'categorie.html',{'categorie':cat,'title':title[cat]})
