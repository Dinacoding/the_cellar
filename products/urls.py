
from django.urls import path
from django.http import HttpResponse
# A simple view function for demonstration

def home_view(request):
    return HttpResponse("Home page is working!")

urlpatterns = [
    path('', home_view, name='home'),
]