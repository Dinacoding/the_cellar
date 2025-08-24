from django.shortcuts import render,redirect,reverse, get_object_or_404
from products.models import Wine
from django.contrib import messages
from django.db.models import Q


# Create your views here.
def all_wines(request):
    """Render the wine index page."""
    wines = Wine.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('all_wine'))
            wines = wines.filter(Q(name__icontains=query) | Q(description__icontains=query))

    context = {       #create a context dictionary to pass data to the template
        'wines': wines,
        'search_term': query,
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

