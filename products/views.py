from django.shortcuts import get_object_or_404, render
from .models import Product
from .models import Category
from cart.models import Entry, Cart 


# Create your views here.

def product(request, product_id):
   
    product = get_object_or_404(Product, pk=product_id)
    

    categories = Category.objects.all()
    user_id = request.user.id
    cart = Cart.objects.values('user').filter(user=user_id)
    context = {
        'product': product,
        'categories': categories,   
        'cart': cart     
    }
    return render(request, 'products/product.html', context)

