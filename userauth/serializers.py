from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from .models import User

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
    
        token['user'] ={ 
            'email':user.email, 
            'username': user.username,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'is_verified':user.is_verified
            }
    
        return token
    
class UserSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = User 
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'is_verified']
