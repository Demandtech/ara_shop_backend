from rest_framework import serializers
from .models import Cart

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        
        fields = ['id', 'name', 'quantity', 'product_id', 'color', 'image', 'price', 'category', 'subtotal']
        read_only_fields =['subtotal']

