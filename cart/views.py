from django.shortcuts import redirect, render
from .models import Entry, Cart
from products.models import Product
from django.contrib import messages
from decimal import Decimal
from django.contrib.auth.models import User

from django.template import RequestContext

# Create your views here.
def entry(request):
    
    if request.method == 'POST':
        user = request.POST['user']
        cart = request.POST['cart']
        product = request.POST['product']
        product_id = request.POST['product_id']
        available_quantity = request.POST['available_quantity']
        product_price = request.POST['product_price']
        quantity = request.POST['quantity']
        
        total_price = int(quantity) * float(product_price)
        print(request)

        if quantity > available_quantity:
            messages.error(request, 'oops you have added more items to your cart that what is in store')
        else:
            if not cart:                
                cart = Cart.objects.create(user = request.user)
                cart.save()
                entry = Entry(product=product, product_price=product_price,quantity=quantity,total_price=total_price, cart=cart)
                entry.save()
           

            

               


            # Access User Id
            # Create a cart if there is no cart ID and I am trying to add a product to cart
            # add an entry with the cart id created or available
            



            # cart_user = User.objects.values('id').filter(id=user)
            # cart = Cart(user = cart_user, total_price = total_price)
            # entry = Entry(user = user, product=product, product_price=product_price,quantity=quantity,total_price = total_price)
            # entry.save()
            
            # entry_user = Entry.objects.values('user')
           
            

           
            

            

            # cart.save()
            messages.success(request, "Successfully added to cart")
        
            #get entry items


    return redirect('/products/'+product_id)
        

# def get_cart_count(request):
#     cart = get_user_cart(request)
#     total_count = 0
#     cart_items = Entry.objects.filter(cart = cart)
#     for item in cart_items:
#         total_count += item.quantity
#     return total_count



