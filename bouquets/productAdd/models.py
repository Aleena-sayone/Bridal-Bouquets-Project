from django.db import models
from productAdd.choices import *
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=100)
    bouqet_type = models.IntegerField(choices=BOUQUETS_CHOICES, default=1)
    price = models.DecimalField(max_digits=10,decimal_places=3)
    flower_type = models.IntegerField(choices=FLOWER_CHOICES, default=1)
    image = models.ImageField(upload_to='product_pics', null=False)
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('productAdd:listproducts')

    def get_url(self):
        return reverse('cart:cart')

class Order(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE)
    products = models.ManyToManyField(Product, default = 0, related_name='products', blank=True)
    order_date = models.DateTimeField(auto_now_add=True)

  



