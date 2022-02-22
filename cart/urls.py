from django.urls import path
from . import views

urlpatterns =[
    path('cart', views.view_cart, name='cart'),
    path('entry', views.entry, name='entry'),
    path('checkout',views.checkout, name='checkout'),
    
]