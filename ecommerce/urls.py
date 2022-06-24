from django.urls import path
from . import views

urlpatterns = [
    path('',views.Home.as_view(),name='home'),
    path('products/', views.Products.as_view(),'products'),
    path('single_product/', views.SingleProduct.as_view(),'single_product'),
    path('contact_us/', views.Contact.as_view(),'contact_us'),
    path('about_us/', views.About.as_view(),'about_us'),
    path('categorie/<str:cat>',views.Categorie.as_view(),name='categorie'),

]
