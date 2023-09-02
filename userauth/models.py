from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, first_name, last_name, email, username, password=None):
        if not email:
            raise ValueError("User must have an email")
        if not username:
            raise ValueError("User must have an username")
        
        email = self.normalize_email(email)
        email = email.lower()
        username = username.lower()

        user = self.model(
            first_name = first_name,
            last_name = last_name,
            email = email,
            username = username
        )

        user.set_password(password)
        user.save(using=self._db)
        
        return user
    
    def create_superuser(self, first_name, last_name, email, username, password=None):
       user = self.create_user(
           email,
           first_name,
           last_name,
           username,
           password=password
       )
       user.is_staff = True
       user.is_superuser = True
       user.save(using=self._db)

class User(AbstractBaseUser, PermissionsMixin):
    is_verified = models.BooleanField(default=False)
    email = models.EmailField(unique=True, max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    username = models.CharField(max_length=255, unique=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email']

    def __str__(self):
        return self.username