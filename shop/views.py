from django.shortcuts import render
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
            'wine': wine,
            'quantity': quantity,
            'subtotal': subtotal,
        })
    
    context = {
        'cart_items': cart_items,
        'total': total,
    }

    return render(request, 'cart.html', context)