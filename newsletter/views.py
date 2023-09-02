from rest_framework.decorators import api_view
from .serializers import NewsLetterSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import NewsLetter


@api_view(['POST'])
def newsletter(request):
    serializer = NewsLetterSerializer(data=request.data)
    if serializer.is_valid():
        email = serializer.validated_data['email']

        if NewsLetter.objects.filter(email=email).exists():
           return Response({"message": "Email already exists"}, status=status.HTTP_400_BAD_REQUEST)  
        serializer.save()
        return Response({"message": "Thank you for subscribing"}, status=status.HTTP_200_OK)
    
    return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)