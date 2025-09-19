from django.urls import path
from . import views

urlpatterns = [
     path('shop/', views.shop_home, name='shop_home'),
     path('cart/', views.view_cart, name='view_cart'),
]