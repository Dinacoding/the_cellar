
from django.urls import path
from django.http import HttpResponse
from . import views 
# A simple view function for demonstration

def home_view(request):
    return HttpResponse("Home page is working!")

urlpatterns = [
    path('', views.all_wines, name='wines'),  
    path('all_categories/', views.all_categories, name='categories'),
    path('<int:wine_id>/', views.wine_detail, name='wine_detail'),]