from django.contrib import admin
from .models import Cart

# Register your models here.


class CartAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'product_id', 'color',
                    'quantity', 'subtotal', 'created_at', 'updated_at', 'image')


admin.site.register(Cart, CartAdmin)
