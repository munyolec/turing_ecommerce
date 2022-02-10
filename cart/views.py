from html import entities
from math import prod
from django.shortcuts import redirect, render
from pkg_resources import PkgResourcesDeprecationWarning
from .models import Entry, Cart
from products.models import Product
from category.models import Category
from django.contrib import messages
from decimal import Decimal
from django.contrib.auth.models import User


def get_cart_user(request):
    cart = None
    # cart_id = None
    if request.user.is_authenticated:
        try:
            cart = Cart.objects.get(user=request.user)
        except Cart.DoesNotExist:    
            cart = Cart(user=request.user) 
            cart.save()
    return cart        


def get_cart_count(request):
    cart = get_cart_user(request)
    total_count = 0
    cart_items = Entry.objects.filter(cart = cart)
    for item in cart_items:
        total_count += item.quantity
    return total_count

def update_item_count(request):
    cart = get_cart_user(request)
    cart_items = Entry.objects.all().filter(cart=cart)
    quantity = Entry.objects.values('quantity').filter(cart = cart)
    for item in cart_items:
        if item in cart_items:
            quantity +=quantity
    return quantity        

def view_cart(request):
    cart = get_cart_user(request)
    cart_items = Entry.objects.filter(cart=cart)
    categories = Category.objects.all()
    order_total = Decimal(0.0)
    for item in cart_items:
        order_total += (item.total_price)


    context = {
        'cart': cart,
        'cart_items': cart_items,
        'order_total': order_total,
        'categories': categories
    }    

    return render(request, 'cart/cart.html',context)

   
# Create your views here.
def entry(request):
    if request.method == 'POST':
        cart = get_cart_user(request)
        product = request.POST['product']
        product_id = request.POST['product_id']
        product_photo = request.POST['product_photo']
        available_quantity = request.POST['available_quantity']
        product_price = request.POST['product_price']
        quantity = request.POST['quantity']
        total_price = int(quantity) * float(product_price)

        # check if number of added items are in stock
        if quantity > available_quantity:
            messages.error(request, 'oops you have added more items to your cart that what is in store')
        else:
            cart_items = Entry.objects.filter(cart=cart)
            product_exists = cart_items.all().filter(product__iexact=product)
            #We should check if prod exits, if it does, we update the quantity
            if product_exists:
                for prod in product_exists:
                    prod_quantity = prod.quantity
                    quantity =int(quantity)
                    # We assume it is one so we just update the quantity
                    prod_quantity += quantity
                    Entry.objects.filter(product__iexact=product).update(quantity=prod_quantity)
                    messages.success(request, "Product quantity updated")
            #exit the loop
           
            #If it doesn't, then we create a new entry
            else:
                entry = Entry.objects.create(product=product, photo_main=product_photo,product_price=product_price,quantity=quantity,total_price=total_price, cart=cart)
                entry.save()
                messages.success(request, "Successfully added to cart")

    return redirect('/products/'+product_id)
        
def checkout(request):



    return render(request, 'cart/checkout.html')        