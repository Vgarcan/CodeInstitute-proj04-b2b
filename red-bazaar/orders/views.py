from django.shortcuts import render, redirect
from .models import Order, OrderItem, ShipAddr
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

    # Extract address data based on the form submission
    form_type = request.POST.get('form_type')

    address_data = {
        'username': request.user.username,
        'full_name': request.POST.get('full_name') if form_type == 'profile' else request.POST.get('alt_full_name'),
        'email': request.POST.get('email') if form_type == 'profile' else request.POST.get('alt_email'),
        'address': request.POST.get('address') if form_type == 'profile' else request.POST.get('alt_address'),
        'city': request.POST.get('city') if form_type == 'profile' else request.POST.get('alt_city'),
        'country': request.POST.get('country') if form_type == 'profile' else request.POST.get('alt_country'),
        'postal_code': request.POST.get('postal_code') if form_type == 'profile' else request.POST.get('alt_postal_code'),
        'phone_number': request.POST.get('phone_number') if form_type == 'profile' else request.POST.get('alt_phone_number'),
    }

    #! ### TEST ###
    for item in address_data.values():
        print(item)
    #! ### TEST ###

    # Extract the products and quantities from the shopping cart dictionary
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
            total_price=total_price,
        )

        # Create the shipping address and assign the instance directly
        ship_address = ShipAddr.objects.create(order=order, **address_data)
        order.ship_address = ship_address
        order.save()

        # Create OrderItem instances for each product in the order
        for item in items:
            OrderItem.objects.create(
                order=order,
                product=item['product'],
                quantity=item['quantity'],
                item_total=item['subtotal']
            )
            # Remove the product quantity from database
            item['product'].quantity -= item['quantity']
            item['product'].save()

    # Clear the shopping cart session
    del request.session['shopping_cart']
    request.session.modified = True

    print("------------------------------------------")
    # Redirect to an order confirmation page or dashboard
    return redirect('orders:confirmation')  # Redirect to order confirmation


@role_required('BUY')
def confirm_order(request):
    """
    Displays the order confirmation page with the user's orders.

    Parameters:
    - request (HttpRequest): The request object, which contains session data and the logged-in user.
        This object is passed by Django's view system and contains information about the current request.

    Returns:
    - HttpResponseRedirect: Redirects to the user's dashboard after displaying the order confirmation page.
        The function uses Django's `redirect` function to redirect the user to the 'users:dashboard' URL.
        The `messages.success` function is used to display a success message to the user.
    """
    messages.success(request, "Your orders have been successfully created!")

    return redirect('users:dashboard')


@role_required('BUY')
def order_detail(request, order_id):
    """
    Displays the details of a specific order.

    Parameters:
    - request (HttpRequest): The request object, which contains session data and the logged-in user.
    - order_id (int): The unique identifier of the order to be displayed.

    Returns:
    - HttpResponse: Renders the 'orders/order_detail.html' template with the order and its associated order items.
    """
    order = Order.objects.get(id=order_id)
    order_items = OrderItem.objects.filter(order=order)
    return render(request, 'orders/order-detail.html', {'order': order, 'order_items': order_items})


@role_required('SUP')
def supplier_order_detail(request, order_id):
    """
    Allows a supplier to view and update the status of a specific order.

    Parameters:
    - request (HttpRequest): The request object, which contains session data and the logged-in user.
    - order_id (int): The unique identifier of the order to be viewed or updated.

    Returns:
    - HttpResponse: Renders the 'orders/supplier_order_detail.html' template with the order and its associated order items.
    If the request method is POST, it also updates the order status based on the provided 'status' parameter.
    If the new status is valid, it saves the changes and displays a success message.
    If the new status is invalid, it displays an error message.
    """
    order = Order.objects.get(
        # Ensures that only the Supplier sees their orders
        id=order_id, seller=request.user)
    order_items = OrderItem.objects.filter(order=order)

    if request.method == "POST":
        new_status = request.POST.get("status")
        if new_status in dict(Order.STATUS_CHOICES).keys():  # Validates the new status
            order.status = new_status
            order.save()
            messages.success(request, "Order status updated successfully.")
        else:
            messages.error(request, "Invalid status selected.")

    return render(request, 'orders/supplier-order-detail.html', {
        'order': order,
        'order_items': order_items
    })


@role_required('SUP')
def update_order(request, order_id, order_status):
    """
    Allows a supplier to update the status of an order.

    Parameters:
    - request (HttpRequest): The request object, which contains session data and the logged-in user.
    - order_id (int): The unique identifier of the order to be updated.
    - order_status (str): The new status to be assigned to the order.

    Returns:
    - HttpResponseRedirect: Redirects to the user's dashboard after updating the order status.
    If the order is successfully updated, a success message is displayed.
    """
    # Ensures that only the Supplier can update their orders
    order = Order.objects.get(id=order_id, seller=request.user)
    order.status = order_status
    order.save()
    messages.success(request, "Order status updated!")
    return redirect('users:dashboard')
