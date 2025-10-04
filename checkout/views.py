from django.shortcuts import render, redirect
from django.contrib import messages
from products.models import Wine
# Create your views here.
def checkout(request):
    if request.method == 'POST':
        # Process the checkout form
        # For simplicity, we'll just clear the cart and show a success message
        if 'cart' in request.session:
            del request.session['cart']
        messages.success(request, "Checkout successful! Thank you for your purchase.")
        return redirect('home')  # Redirect to home or order confirmation page

    return render(request, 'checkout.html')