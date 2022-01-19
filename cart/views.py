from django.shortcuts import redirect, render
from .models import Entry, Cart, Product
from django.contrib import messages


# Create your views here.
def entry(request):
    if request.method == 'POST':
        product = request.POST['product']
        print(product)
        product_id = request.POST['product_id']
        available_quantity = request.POST['available_quantity']
        product_price = request.POST['product_price']
        quantity = request.POST['quantity']

        total_price = int(quantity) * float(product_price)

        if quantity > available_quantity:
            messages.error(request, 'oops you have added more items to your cart that what is in store')

        else:
            entry = Entry(product=product, product_price=product_price,quantity=quantity,total_price = total_price)
            entry.save()
            messages.success(request, "Successfully added to cart")
      

    return redirect('/products/'+product_id)
        
