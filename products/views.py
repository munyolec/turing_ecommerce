from django.shortcuts import get_object_or_404, render
from .models import Product

# Create your views here.
def index(request):
    
    
    return render(request, 'pages/index.html') 


def product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    context = {
        'product': product
    }

    return render(request, 'products/product.html', context)