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