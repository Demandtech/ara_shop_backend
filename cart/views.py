from .models import Cart
from .serializers import CartSerializer
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def cart(request):
    user = request.user
    if request.method == 'POST':
        existing_cart_item = Cart.objects.filter(
            user=user, 
            product_id=request.data['product_id'], 
            color=request.data['color']).first()
      
        if existing_cart_item:
            return Response({"message": "Item already in the cart."}, status=status.HTTP_400_BAD_REQUEST)


        serializer = CartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=user)
            return Response({"message":"Item add successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    carts = user.cart_set.all()
    total_items = len(carts)
    cart_subtotal = sum(cart.subtotal for cart in carts)
    serializer = CartSerializer(carts, many=True)
    return Response({"cart": serializer.data, "total_items":total_items, "subtotal":cart_subtotal}, status=status.HTTP_200_OK)


@api_view(['DELETE', 'PUT'])
@permission_classes([IsAuthenticated])
def remove_cart(request, pk):
    user = request.user
    if request.method == 'DELETE':
        try:
            cart_item = user.cart_set.get(id=pk)
            cart_item.delete()
            return Response({"message":"Cart item deleted"}, status=status.HTTP_200_OK)
        except Cart.DoesNotExist:
            return Response({"message":"Cart item not found"}, status=status.HTTP_404_NOT_FOUND)
    try: 
        cart = Cart.objects.get(id=pk)
    except Cart.DoesNotExist:
        return Response({"message": "cart with the provided ID does not exist."})
    serializer = CartSerializer(cart, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Cart item updated!"}, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)