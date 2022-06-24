from django.contrib import admin

from .models import Products
from .models import Tags


from .models import Client
from .models import Categories
from .models import Commande






admin.site.register(Products)

admin.site.register(Tags)



admin.site.register(Client)
admin.site.register(Categories)
admin.site.register(Commande)






# Register your models here.
