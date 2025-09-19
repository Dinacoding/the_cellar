from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from products.models import Wine

# Create your views here.

def shop_home(request):
    wines = Wine.objects.all()
    print(f"Number of wines found: {wines.count()}")
    print(f"Wines in queryset: {list(wines)}")
    context = {
        'wines': wines
    }
    return render(request, 'shop_home.html', context)

def add_to_cart(request, wine_id):
    """ Add wine to cart """
    if request.method == 'POST':
        cart = request.session.get('cart', {})
        quantity = int(request.POST.get('quantity', 1))

        if str(wine_id) in cart:
            cart[str(wine_id)] += quantity
        else:
            cart[str(wine_id)] = quantity

        request.session['cart'] = cart
        messages.success(request, 'Item added to cart!')

    return redirect('view_cart')

def view_cart(request):
    """ A view to render the shopping cart contents. """
    cart = request.session.get('cart', {})
    cart_items = []
    total = 0

    for item_id, quantity in cart.items():
        wine = get_object_or_404(Wine, pk=item_id)
        subtotal = quantity * wine.price
        total += subtotal
        cart_items.append({
            'item_id': item_id,
            'wine': wine,
            'quantity': quantity,
            'subtotal': subtotal,
        })

    context = {
        'cart_items': cart_items,
        'total': total,
    }

    return render(request, 'cart.html', context)

def update_cart(request, item_id):
    """Update the quantity of the specified product in the shopping cart"""
    if request.method == 'POST':
        # Get the new quantity from the form
        quantity = int(request.POST.get('quantity'))
        cart = request.session.get('cart', {})
        
        # Ensure the item is in the cart and update the quantity
        if str(item_id) in cart:
            cart[str(item_id)] = quantity
            request.session['cart'] = cart
            messages.success(request, 'Cart updated successfully!')
            
    return redirect('view_cart')

def remove_from_cart(request, item_id):
    """ Remove an item from the shopping cart.
    """
    if request.method == 'POST':
        cart = request.session.get('cart', {})
        
        # Remove the item if it exists in the cart
        if str(item_id) in cart:
            del cart[str(item_id)]
            request.session['cart'] = cart
            messages.success(request, 'Item removed from cart!')
            
    return redirect('view_cart')