from django.db import models
from django import forms

# Create your models here.
class Product(models.Model):
    CHOICES_CATEGORY = [('men', 'Men'),('women', 'Women'),('accessory', 'Accessory')]

    name = models.CharField(max_length=500)
    category = models.TextField(choices=CHOICES_CATEGORY)
    price = models.FloatField()
    stars = models.FloatField()
    bonus = models.FloatField()
    featured = models.BooleanField(default=False)
    best_seller = models.BooleanField(default=False)
    desc = models.TextField()
    colors = models.JSONField(null=True, blank=True, default=list)
    images = models.JSONField()
    sizes = models.JSONField(null=True, blank=True, default=list)
