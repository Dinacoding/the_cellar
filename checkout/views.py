from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.urls import reverse


# Create your views here.
def checkout(request):
    if request.method == 'POST':
        # Process the checkout form
        # For simplicity, we'll just clear the cart and show a success message
        if 'cart' in request.session:
            del request.session['cart']
        messages.success(request, "Checkout successful! Thank you for your purchase.")
        return redirect('home')  # Redirect to home or order confirmation page

    return render(request, 'checkout/checkout.html')