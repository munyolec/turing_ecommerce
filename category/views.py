from django.shortcuts import render
from django.shortcuts import get_object_or_404, render

from category.models import Category
from products.models import Product

# Create your views here


def category(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    context = {
        'category': category
    }

    return render(request, 'categories/category.html', context)