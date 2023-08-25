from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.authentication import TokenAuthentication
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import MyTokenObtainPairSerializer, UserSerializer
from .models import User

@api_view(['POST'])
@permission_classes([AllowAny])
@authentication_classes([TokenAuthentication])
def register(request):
    serializer = UserSerializer(data = request.data)
    if serializer.is_valid():
        email = serializer.validated_data['email']
        if User.objects.filter(email=email).exists():
            return Response({"detail": "User with email already exists"}, status=status.HTTP_400_BAD_REQUEST)
        user = serializer.save()
        
        refresh = RefreshToken.for_user(user)

        refresh['user'] ={ 
            'email':user.email, 
            'username': user.username,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'is_verified':user.is_verified
            }
        
        token_serializer = MyTokenObtainPairSerializer(data={"username":user.username, "password":user.password})
        token_serializer.is_valid()
        access_token = token_serializer.get_token(user)
        refresh_token = str(refresh)
        return Response({"access":str(access_token), "refresh": refresh_token}, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer