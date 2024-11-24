import stripe
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from users.models import Profile
from utils import sup_dict

stripe.api_key = settings.STRIPE_SECRET_KEY


@login_required
def checkout(request):
    """
    View for displaying the checkout page and handling the payment process.
    Redirects the user to the product list if the shopping cart is empty.

    Parameters:
    request (HttpRequest): The request object containing the user's session and other information.

    Returns:
    HttpResponse: The rendered checkout page with initial data, cart items, and client secret for PaymentIntent.
    If the shopping cart is empty, redirects to the product list page.
    """
    # Get the shopping cart from the session
    shopping_cart = request.session.get('shopping_cart', {})

    # Check if the shopping cart is empty
    if not shopping_cart:
        # Redirect to the product list page if the cart is empty
        return redirect('products:all')

    # Group the cart items by seller using the sup_dict function
    cart_items = sup_dict(shopping_cart, source="cart")
    total_cost = sum(item['subtotal']
                     for items in cart_items.values() for item in items)

    # Get the current user's profile data to pre-fill the form
    try:
        profile = Profile.objects.get(user=request.user)
        initial_data = {
            'full_name': profile.full_name,
            'email': request.user.email,
            'address': profile.address,
            'city': profile.city,
            'country': profile.country,
            'postal_code': profile.postal_code,
            'phone_number': profile.phone_number,
        }
    except Profile.DoesNotExist:
        initial_data = {}

    # Create a PaymentIntent with the total cost in cents (Stripe uses the smallest currency unit)
    intent = stripe.PaymentIntent.create(
        amount=int(total_cost * 100),  # Convert dollars to cents
        currency='usd',
        automatic_payment_methods={
            'enabled': True,
        },
        metadata={'user_id': request.user.id}
    )

    print("Client secret:", intent.client_secret)

    # Render the template with initial data, cart items, and client secret for PaymentIntent
    return render(request, 'payments/checkout.html', {
        'initial_data': initial_data,
        'STRIPE_PUBLIC_KEY': settings.STRIPE_PUBLIC_KEY,
        'cart_items': cart_items,
        'total_cost': total_cost,
        'client_secret': intent.client_secret  # Send the client secret to the frontend
    })


def payment_success(request):
    return render(request, 'payments/success.html')
