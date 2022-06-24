from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

# # Create your views here.

class Home(View):
    def get(self,response):
        return render(response,'index.html')

def Products(request):
    return render(request, 'products.html')

def SingleProduct(request):
    return render(request, 'single-product.html')

def Contact(request):
    return render(request, 'contact.html')

def About(request):
    return render(request, 'about.html')

