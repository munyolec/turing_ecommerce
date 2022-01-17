from django.shortcuts import render
from products.models import Product
from category.models import Category

# Create your views here.
def index(request):
    products=Product.objects.all()
    categories = Category.objects.all()
    context ={
        'products': products,
        'categories':categories
    }
    
    return render(request, 'pages/index.html',context)


def about(request):
    products=Product.objects.all()
    context ={
        'products': products
    }
    
    return render(request, 'pages/about.html', context)    


def categories(request):
    categories=Category.objects.all()
    context ={
        'categories': categories
    }
    
    return render(request, 'pages/categories.html', context)     