from django.shortcuts import render
from products.models import Wine
from products.models import Category
from django.http import HttpResponse
# Create your views here.
def index(request):
    """Render the home page."""

    return render(request, 'home/index.html')

def all_wines(request):
    """Render the wine index page."""
    wines = Wine.objects.all()
    context = {  # create a context dictionary to pass data to the template
        'wines': wines,
    }
    return render(request, 'products.html', context)