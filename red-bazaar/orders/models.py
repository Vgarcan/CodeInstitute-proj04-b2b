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
        ship_address (ForeignKey): Recorded address for the shipment.
        status (str): The current status of the order.
    """
    buyer = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name="orders_as_buyer")
    seller = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name="orders_as_seller")
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    ship_address = models.ForeignKey(
        "ShipAddr", on_delete=models.CASCADE, related_name="buyer_addr", blank=True, null=True)
    ordered_on = models.DateTimeField(default=timezone.now)

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
        ('processing', 'Processing'),
        ('delivered', 'Delivered'),
        ('shipped', 'Shipped'),
    ]
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"Order #{self.id} | Buyer: {self.buyer.username} | Seller: {self.seller.username} | Status: {self.status} | Total: £{self.total_price}"


class ShipAddr(models.Model):
    """
    Represents a shipping address for an order.

    Attributes:
        order (ForeignKey): The order associated with this shipping address.
        username (str): The name of the recipient.
        email (str): The email of the recipient.
        address (str): The street address of the recipient.
        city (str): The city for the shipping address.
        country (str): The country for the shipping address.
        postal_code (str): The postal code of the shipping address.
        phone_number (str): The contact number for the recipient.
    """
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name="buyers_address")
    username = models.CharField(max_length=255, default="NOT INCLUDED")
    email = models.EmailField(max_length=255, default="NOT INCLUDED")
    address = models.CharField(max_length=255, default="NOT INCLUDED")
    city = models.CharField(max_length=255, default="NOT INCLUDED")
    country = models.CharField(max_length=255, default="NOT INCLUDED")
    postal_code = models.CharField(max_length=10, default="NOT INCLUDED")
    phone_number = models.CharField(max_length=20, default="NOT INCLUDED")

    def __str__(self):
        return f"{self.username} - {self.address}, {self.city}, {self.country}"


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
        return f"Order #{self.order.id} | {self.quantity}x {self.product.name} - Item Total: £{self.item_total}"
