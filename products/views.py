from django.shortcuts import render

# Create your views here.
def index(request):
    """Render the wine index page."""
    return render(request, 'products/index.html')
