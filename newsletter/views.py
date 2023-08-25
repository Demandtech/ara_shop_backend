from rest_framework.decorators import api_view
from .serializers import NewsLetterSerializer
from .models import NewsLetter
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

@api_view(['POST'])
def newsletter(request):
    serializer = NewsLetterSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Thank you for subscribing"}, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)