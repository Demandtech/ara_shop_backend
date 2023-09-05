from django.urls import path
from . import views

urlpatterns = [
    path('', views.product),
    path('<int:pk>', views.product_detail),
    path('category/<str:category>/', views.category_product),
    path('best_sellers/', views.best_seller),
    path('featured/', views.featured),
    path('search/', views.search_products),
    path('filter/', views.filtered_products)
]
