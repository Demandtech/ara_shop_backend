from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    is_verified = models.BooleanField(default=False)
    email = models.EmailField(unique=True)