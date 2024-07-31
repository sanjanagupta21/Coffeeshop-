from django.shortcuts import render, redirect
from .models import CartItem

def home_view(request):
    return render(request, 'home.html')

def menu_view(request):
    return render(request, 'menu.html')

def add_to_cart(request):
    item_id = request.POST.get('item_id')
    if item_id:
        cart_item, created = CartItem.objects.get_or_create(item_id=item_id)
        if not created:
            cart_item.quantity += 1
        cart_item.save()
    return redirect('menu')

def view_cart(request):
    cart_items = CartItem.objects.all()
    return render(request, 'cart.html', {'cart_items': cart_items})
def menu_view(request):
    quantities = list(range(16))  # Creates a list [0, 1, 2, ..., 15]
    return render(request, 'menu.html', {'quantities': quantities})
from django.shortcuts import render, get_object_or_404, redirect
from app.models import Product, CartItem

from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product, CartItem

@login_required
def add_to_cart(request):
    if request.method == 'POST':
        item_id = request.POST.get('item_id')
        quantity = request.POST.get('quantity')

        product = get_object_or_404(Product, id=item_id)

        # Check if the item is already in the cart
        cart_item, created = CartItem.objects.get_or_create(
            user=request.user,
            product=product,
            defaults={'quantity': quantity}
        )

        if not created:
            # Update quantity if item already exists
            cart_item.quantity += int(quantity)
            cart_item.save()

        return redirect('menu')
