from django.shortcuts import get_object_or_404, render
from .models import Product
from .models import Category

# Create your views here.

def product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    categories = Category.objects.all()
    context = {
        'product': product,
        'categories': categories

    }
    return render(request, 'products/product.html', context)

