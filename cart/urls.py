from django.urls import path
from . import views

urlpatterns = [
    path('cart', views.cart),
    path('cart/<int:pk>', views.remove_cart)
]