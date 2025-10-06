from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.conf import settings


from products.models import Wine, Category



import stripe

from products.models import Wine
# Create your views here.

def checkout(request):
    # Ensure Stripe is initialized (keys are loaded in settings.py)
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    stripe.api_key = stripe_secret_key

    if request.method == 'POST':
        if 'cart' in request.session:
            # Clear the cart ONLY after successfully saving the order to the database
            del request.session['cart']
        
        # Use a descriptive message.
        messages.success(request, "Payment received and order confirmed! Thank you.")
        
        # Redirect to a dedicated order success/history page.
        return redirect('home') 

    else: # GET request: Load data and create Payment Intent

        cart_items = []
        total = 0
        cart = request.session.get('cart', {}) 
        # CART CHECK
        if not cart:
            messages.error(request, "There's nothing in your cart to checkout.")
            # Redirect to the product listing page
            return redirect('all_wines') 
        # BUILD CURRENT CART
        for item_id, quantity in cart.items():
            wine = get_object_or_404(Wine, pk=item_id)
            subtotal = float(wine.price) * quantity
            total += subtotal

            cart_items.append({
                'wine': wine,
                'quantity': quantity,
                'subtotal': subtotal,
            })
            
        total_cents = round(total * 100)
        current_cart = {
            item_id: {
                'wine': get_object_or_404(Wine, pk=item_id),
                'quantity': quantity,
                'subtotal': float(get_object_or_404(Wine, pk=item_id).price) * quantity
            }
            for item_id, quantity in cart.items()
        }
        # DEBUGGING OUTPUT
        print(f"Current cart structure: {current_cart}")

        # STRIPE PAYMENT INTENT CREATION
        try:
            intent = stripe.PaymentIntent.create(
                amount=total_cents,
                currency=settings.STRIPE_CURRENCY, # Define STRIPE_CURRENCY in settings.py
            )
        except Exception as e:
            # Handle API errors gracefully
            messages.error(request, f"Stripe API Error: A payment setup error occurred. Please try again. ({e})")
            # Fallback to the cart view
            return redirect('view_cart') 

        # RENDER TEMPLATE
    context = {
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
        'total': total,
        # Pass the structured data from current_cart
        'cart_items': list(current_cart.values()),
        'cart_total': total,
    }
    return render(request, 'checkout.html', context)

