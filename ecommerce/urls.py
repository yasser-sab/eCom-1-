from django.urls import path
from . import views

urlpatterns = [
    path('',views.Home.as_view(),name='home'),
    path('categorie/<str:cat>',views.Categorie.as_view(),name='categorie'),
]
