from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

class Cart(models.Model):
    CHOICES_SIZES = [('normal', 'Normal'),('s', 'Small'),('m', 'Medium'),('l', 'Large'), ('xl', 'Extra Large')]
    CHOICES_CATEGORY = [('men', 'Men'),('women', 'Women'),('accessory', 'Accessory')]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=500)
    quantity = models.IntegerField(null=False)
    subtotal = models.FloatField(null=False)
    product_id = models.IntegerField()
    color = models.CharField(max_length=100)
    image = models.CharField(max_length=500)
    price = models.FloatField(null=False)
    category =  models.TextField(choices=CHOICES_CATEGORY)
    size = models.TextField(choices=CHOICES_SIZES)

    def save(self, *args, **kwargs):
        self.subtotal = self.price * self.quantity
        super().save(*args, **kwargs)