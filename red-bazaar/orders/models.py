from django.db import models

# Create your models here.


class ShoppingList(models.Model):
    buyer = models.ForeignKey('users.CustomUser', on_delete=models.PROTECT)
    product_id = models.ManyToManyField('products.Product')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Shopping list for {self.buyer}"


class OrderList(models.Model):
    buyer = models.ForeignKey(
        'users.CustomUser', on_delete=models.PROTECT, related_name='order_lists_as_buyer')
    seller = models.ForeignKey(
        'users.CustomUser', on_delete=models.PROTECT, related_name='order_lists_as_seller')
    shoppinglist_id = models.OneToOneField(
        ShoppingList, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    ordered_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order list between {self.buyer} and {self.seller}"
