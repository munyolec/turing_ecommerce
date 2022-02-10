from django.urls import path
from . import views

urlpatterns= [
    path('<int:category_id>', views.category, name='category'),
    path('cat_product', views.cat_product, name='cat_product'),

   
   
]