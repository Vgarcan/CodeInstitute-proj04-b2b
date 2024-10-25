from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from products.models import Product

User = get_user_model()


class Order(models.Model):
    """
    Represents an individual order placed by a buyer for products from a specific seller.

    Attributes:
        buyer (ForeignKey): Reference to the buyer user placing the order.
        seller (ForeignKey): Reference to the seller from whom the buyer purchases products.
        total_price (Decimal): Total amount for this order.
        ordered_on (DateTimeField): Timestamp when the order was placed.
        status (str): The current status of the order.
    """
    buyer = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name="orders_as_buyer")
    seller = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name="orders_as_seller")
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    ordered_on = models.DateTimeField(default=timezone.now)

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('canceled', 'Canceled'),
    ]
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"{str(self.buyer).upper()} from {str(self.seller).upper()} on {self.ordered_on}"


class OrderItem(models.Model):
    """
    Represents an item in an order, linking a specific product to an order.

    Attributes:
        order (ForeignKey): Reference to the order this item belongs to.
        product (ForeignKey): Reference to the product purchased.
        quantity (Integer): Quantity of the product in the order.
        item_total (Decimal): Total price for this specific item, calculated by quantity * product price.
    """
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField()
    item_total = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        # Calculate item total before saving
        self.item_total = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.quantity} of {str(self.product.name).upper()} for {self.order}"
