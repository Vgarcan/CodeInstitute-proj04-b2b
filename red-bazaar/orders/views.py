from django.shortcuts import render, redirect
from .models import Order, OrderItem
from products.models import Product
from django.contrib import messages

from users.decorators import role_required
from utils import sup_dict

# Create your views here.


@role_required('BUY')
def create_order(request):
    """
    Creates an order based on the user's current shopping cart. 
    Each item in the cart is converted into an OrderItem, and an Order 
    is created for each seller involved in the transaction.

    Parameters:
    - request (HttpRequest): The request object, which contains session data and the logged-in user.

    Returns:
    - HttpResponse: Redirects to the order confirmation page or the user's order dashboard.
    """
    print("------------------------------------------")
    # shopping cart from the session
    shopping_cart = request.session.get('shopping_cart', {})

    if not shopping_cart:
        messages.warning(request, "Your cart is empty.")
        # Redirect to product list if cart is empty
        return redirect('products:all')

    cart_items = sup_dict(shopping_cart, source="cart")

    print('ORDERS - VIEWS.PY - create_order | cart_items.items(): ',
          cart_items.items())
    # Create an order for each seller in the cart
    for seller_id, items in cart_items.items():
        # Calculate total price for the order
        total_price = sum(item['subtotal'] for item in items)

        # Create the Order instance
        order = Order.objects.create(
            buyer=request.user,
            seller_id=seller_id.id,
            total_price=total_price
        )

        # Create OrderItem instances for each product in the order
        for item in items:
            OrderItem.objects.create(
                order=order,
                product=item['product'],
                quantity=item['quantity'],
                item_total=item['subtotal']
            )

    # Clear the shopping cart session
    del request.session['shopping_cart']
    request.session.modified = True

    print("------------------------------------------")
    # Redirect to an order confirmation page or dashboard
    messages.success(request, "Your orders have been successfully created!")
    return redirect('orders:confirmation')  # Redirect to order confirmation


@role_required('BUY')
def confirm_order(request):
    """
    Displays the order confirmation page with the user's orders.
    """
    messages.success(request, "Order confirmation!")

    return redirect('main:home')


@role_required('BUY')
def order_detail(request, order_id):
    """
    Displays the details of a specific order.
    """
    order = Order.objects.get(id=order_id)
    order_items = OrderItem.objects.filter(order=order)
    return render(request, 'orders/order_detail.html', {'order': order, 'order_items': order_items})


@role_required('SUP')
def update_order(request, order_id):
    """
    Allows a supplier to update the status of an order.
    """
    order = Order.objects.get(id=order_id)
    order.status = request.POST.get('status')
    order.save()
    messages.success(request, "Order status updated!")
    return redirect('orders:order-detail', order_id=order_id)
