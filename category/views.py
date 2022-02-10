from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404, render

from category.models import Category
from products.models import Product

# Create your views here

def category(request, category_id):
    categories = Category.objects.all()
    category = get_object_or_404(Category, pk=category_id)
    category_products = Product.objects.all().filter(category_id =category)

    context = {
        'categories':categories,
        'category': category,
        'category_products': category_products,
       
    }
    return render(request, 'category/category.html', context)

