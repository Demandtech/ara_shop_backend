from django.urls import path
from . import views

urlpatterns = [
    path('cart/', views.cart),
    path('cart/<int:pk>/', views.remove_cart),
    path('cart/update_cart_list/', views.update_cart_list)
]