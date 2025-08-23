from django.shortcuts import render, get_object_or_404
from products.models import Wine, Category


# Create your views here.
def all_wines(request):
    """Render the wine index page."""
    wines = Wine.objects.all()
    context = {       #create a context dictionary to pass data to the template
        'wines': wines,
    }
    return render(request, 'products.html', context)

def wine_detail(request, wine_id):
    """Render the wine detail page."""
    wine = get_object_or_404(Wine, id=wine_id)
    context = {
        'wine': wine,
    }
    return render(request, 'wine_detail.html', context)

   

def all_categories(request):
    """Render the categories index page."""
    categories = Category.objects.all()
    context = {
        'categories': categories,
    }
    return render(request, 'categories.html', context)

