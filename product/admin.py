from django.contrib import admin
from .models import Product

# Register your models here.

class ProductAmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'bonus', 'featured', 'category', 'stars', 'best_seller')

admin.site.register(Product, ProductAmin)