from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=250, blank=False, null=False)
    description = models.TextField(max_length=250, blank=True, null=True)


class Subcategory(models.Model):
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=250, blank=False, null=False)
    description = models.TextField(max_length=250, blank=True, null=True)


class Product(models.Model):
    seller_id = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory_id = models.ForeignKey(
        Subcategory, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    description = models.TextField(max_length=250, blank=True, null=True)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)
    is_bestseller = models.BooleanField(default=False)
    is_trending = models.BooleanField(default=False)
    rating = models.IntegerField(default=0, null=False, blank=False)
