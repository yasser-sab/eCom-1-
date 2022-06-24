from django.urls import path
from . import views

urlpatterns = [
    path('',views.Home.as_view(),name='home'),
    path('products/', views.Products),
    path('single_product/', views.SingleProduct),
    path('contact_us/', views.Contact),
    path('about_us/', views.About),
]
