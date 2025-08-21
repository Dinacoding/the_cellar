from django.shortcuts import render
from products.models import Wine, Category


# Create your views here.
def all_wines(request):
    """Render the wine index page."""
    wines = Wine.objects.all()
    context = {       #create a context dictionary to pass data to the template
        'wines': wines,
    }
    return render(request, 'products.html', context)

   

def all_categories(request):
    """Render the categories index page."""
    categories = Category.objects.all()
    context = {
        'categories': categories,
    }
    return render(request, 'categories.html', context)

