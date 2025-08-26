from django.shortcuts import render,redirect,reverse, get_object_or_404
from products.models import Wine , Category
from django.contrib import messages
from django.db.models import Q
import django.db.models.functions as models
from django.db.models.functions import Lower
# from django.http import HttpResponse


# Create your views here.
def all_wines(request):
    """Render the wine index page."""
    wines = Wine.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if 'sort' in request.GET:
        sortkey = request.GET['sort']
        # This will get the field name, e.g., 'price' or 'name'
        sort = sortkey
        
        if sortkey == 'name':
            sortkey = 'lower_name'
            wines = wines.annotate(lower_name=Lower('name'))
            
        if 'direction' in request.GET:
            direction = request.GET['direction']
            if direction == 'desc':
                # Prepend the '-' sign for descending order
                sortkey = f'-{sortkey}'
        
        # Finally, order the queryset by the constructed sortkey
        wines = wines.order_by(sortkey)


    if 'category' in request.GET:
        categories = request.GET['category'].split(',')
        wines = wines.filter(category__name__in=categories)
        categories = Category.objects.filter(name__in=categories)

    if 'q' in request.GET:
        query = request.GET['q']
        if not query:
            messages.error(request, "You didn't enter any search criteria!")
            return redirect(reverse('all_wines'))
        wines = wines.filter(Q(name__icontains=query) | Q(description__icontains=query))

    context = {       #create a context dictionary to pass data to the template
        'wines': wines,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': f'{sort}_{direction}',
    

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

