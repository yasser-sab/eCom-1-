from django.urls import path
from . import views

urlpatterns = [
    path('',views.Home.as_view(),name='home'),
    path('products/', views.Products.as_view(),name='products'),
    path('single_product/<int:pr>', views.SingleProduct.as_view(),name='single_product'),
    path('contact_us/', views.Contact.as_view(),name='contact_us'),
    path('about_us/', views.About.as_view(),name='about_us'),
    path('categorie/<str:cat>',views.Categorie.as_view(),name='categorie'),
    path('cart/', views.Cart.as_view(),name='cart'),
    path('cart/<int:id>', views.add,name='cardP'),
]
