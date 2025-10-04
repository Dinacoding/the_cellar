from django.urls import path
from . import views
from django.conf import settings

import stripe


urlpatterns = [
    path('', views.checkout, name='checkout'),
]
