from django.urls import path
from . import views

urlpatterns = [
     path('shop/', views.shop_home, name='shop_home'),
     path('cart/', views.view_cart, name='view_cart'),
     path('add_to_cart/<int:wine_id>/', views.add_to_cart, name='add_to_cart'),
     path('update/<int:item_id>/', views.update_cart, name='update_cart'),
     path('remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
]