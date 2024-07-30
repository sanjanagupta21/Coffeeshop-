from django.shortcuts import render, redirect
from .models import CartItem

def home_view(request):
    return render(request, 'home.html')


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
