from .models import Categories

def extras(request):
    categories=Categories.objects.all()
    return {"Categories":categories}

def cart(request):
    cart=[1,2]
    return {"Cart":cart}