from django.db.models import Count
from django.contrib.auth.decorators import login_required
from .models import Order
from django.db.models import Sum, F
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import Order, OrderItem, ShipAddr
from products.models import OrderProductSnapshot
from django.contrib import messages

from users.decorators import role_required
from utils import sup_dict

# Create your views here.


@role_required("BUY")
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
    shopping_cart = request.session.get("shopping_cart", {})

    if not shopping_cart:
        messages.warning(request, "Your cart is empty.")
        # Redirect to product list if cart is empty
        return redirect("products:all")

    # Extract address data based on the form submission
    form_type = request.POST.get("form_type")

    address_data = {
        "username": request.user.username,
        "full_name": request.POST.get("full_name")
        if form_type == "profile"
        else request.POST.get("alt_full_name"),
        "email": request.POST.get("email")
        if form_type == "profile"
        else request.POST.get("alt_email"),
        "address": request.POST.get("address")
        if form_type == "profile"
        else request.POST.get("alt_address"),
        "city": request.POST.get("city")
        if form_type == "profile"
        else request.POST.get("alt_city"),
        "country": request.POST.get("country")
        if form_type == "profile"
        else request.POST.get("alt_country"),
        "postal_code": request.POST.get("postal_code")
        if form_type == "profile"
        else request.POST.get("alt_postal_code"),
        "phone_number": request.POST.get("phone_number")
        if form_type == "profile"
        else request.POST.get("alt_phone_number"),
    }

    #! ### TEST ###
    for item in address_data.values():
        print(item)
    #! ### TEST ###

    # Extract the products and quantities from the shopping cart dictionary
    cart_items = sup_dict(shopping_cart, source="cart")

    print("ORDERS - VIEWS.PY - create_order | cart_items.items(): ",
          cart_items.items())
    # Create an order for each seller in the cart
    for seller_id, items in cart_items.items():
        # Calculate total price for the order
        total_price = sum(item["subtotal"] for item in items)

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
            # Create a snapshot of the product
            product_snapshot = OrderProductSnapshot.objects.create(
                name=item["product"].name,
                price=item["product"].price,
                description=item["product"].description,
                image=item["product"].image,
                category=item["product"].category_id.name,
            )

            # Create the OrderItem with the snapshot
            OrderItem.objects.create(
                order=order,
                product=product_snapshot,
                quantity=item["quantity"],
                item_total=item["subtotal"],
            )

            # Remove the product quantity from database
            item["product"].quantity -= item["quantity"]
            item["product"].save()

    # Clear the shopping cart session
    del request.session["shopping_cart"]
    request.session.modified = True

    print("------------------------------------------")
    # Redirect to an order confirmation page or dashboard
    return redirect("orders:confirmation")  # Redirect to order confirmation


@role_required("BUY")
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

    return redirect("users:dashboard")


@role_required("BUY")
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
    return render(
        request,
        "orders/order-detail.html",
        {"order": order, "order_items": order_items},
    )


@role_required("SUP")
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
        id=order_id,
        seller=request.user,
    )
    order_items = OrderItem.objects.filter(order=order)

    if request.method == "POST":
        new_status = request.POST.get("status")
        if new_status in dict(Order.STATUS_CHOICES).keys():  # Validates the new status
            order.status = new_status
            order.save()
            messages.success(request, "Order status updated successfully.")
        else:
            messages.error(request, "Invalid status selected.")

    return render(
        request,
        "orders/supplier-order-detail.html",
        {"order": order, "order_items": order_items},
    )


@role_required("SUP")
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
    return redirect("users:dashboard")


@login_required
def chart_data(request, user_role):
    """
    Generate data for Chart.js based on user role (buyer or supplier).

    Args:
        request: HTTP request object.
        user_role (str): Either 'buyer' or 'supplier'.

    Returns:
        JsonResponse: Labels (months) and data (totals).
    """
    if user_role == "buyer":
        queryset = (
            Order.objects.filter(buyer=request.user)
            .annotate(month=F("ordered_on__month"))
            .values("month")
            .annotate(total_spent=Sum("total_price"))
            .order_by("month")
        )
        data = [entry["total_spent"] for entry in queryset]
    elif user_role == "supplier":
        queryset = (
            Order.objects.filter(seller=request.user)
            .annotate(month=F("ordered_on__month"))
            .values("month")
            .annotate(total_earned=Sum("total_price"))
            .order_by("month")
        )
        data = [entry["total_earned"] for entry in queryset]
    else:
        return JsonResponse({"error": "Invalid user role"}, status=400)

    labels = [f"Month {entry['month']}" for entry in queryset]
    return JsonResponse({"labels": labels, "data": data})


@login_required
def transaction_status_data(request):
    """
    Provide data for total transactions grouped by status.
    """
    # Obtener el rol del usuario autenticado
    print(">>>>>>>", request.user.role)
    user_role = request.user.role

    print(">>>>>>>", user_role)

    if user_role == "BUY":
        orders = request.user.orders_as_buyer.all()
    elif user_role == "SUP":
        orders = request.user.orders_as_seller.all()
    else:
        return JsonResponse({"error": "Invalid user role"}, status=400)

    # Anota la cantidad de órdenes por estado
    status_data = orders.values("status").annotate(count=Count("id"))

    # Incluye estados con valor cero para los estados que no tienen órdenes
    all_statuses = dict(Order.STATUS_CHOICES)
    labels = [all_statuses[status] for status in all_statuses]
    data = [
        next((entry["count"]
             for entry in status_data if entry["status"] == status), 0)
        for status in all_statuses
    ]

    return JsonResponse({"labels": labels, "data": data})
