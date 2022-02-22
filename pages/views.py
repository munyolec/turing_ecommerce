from django.shortcuts import render
from products.models import Product
from category.models import Category
from django.core.paginator import Paginator


# Create your views here.
def index(request):
    products=Product.objects.all()

    paginator = Paginator(products,4)
    page = request.GET.get('page')
    paged_products = paginator.get_page(page)
    
    categories = Category.objects.all()
    context ={
        'products': paged_products,
        'categories':categories
    }
    return render(request, 'pages/index.html',context)


def about(request):
    products=Product.objects.all()
    context ={
        'products': products
    }

    return render(request, 'pages/about.html', context)    

