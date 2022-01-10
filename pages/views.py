from django.shortcuts import render
from products.models import Product
# Create your views here.
def index(request):
    products=Product.objects.all()
    context ={
        'products': products
    }
    
    return render(request, 'pages/index.html',context)


def about(request):
    products=Product.objects.all()
    context ={
        'products': products
    }
    
    return render(request, 'pages/about.html', context)    