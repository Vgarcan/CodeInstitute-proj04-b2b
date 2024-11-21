from direct_messages.models import Message
from django.db.models import Q
from products.models import Product
from orders.models import Order, OrderItem


def sup_dict(source_data, source=None):
    """
    Groups products by seller for either a shopping cart or an order.

    Parameters:
    - source_data (dict or QuerySet): Data representing either the shopping cart (dictionary) 
      or an order's items (QuerySet).
    - source (str): Specifies the data source, either 'cart' for shopping cart data or 'order' for order items.

    Returns:
    - dict: A dictionary grouping products by seller, with each product's quantity, subtotal, and other details.
    """
    print("------------------------------------------")
    cart_items = {}

    if source == "cart":  # Used for retreive from SESSION
        # Process as a shopping cart
        # Instantiate products filtering by ID
        products = Product.objects.filter(id__in=source_data.keys())
        print('UTILS.PY - sup_dict | source_data.keys(): ', source_data.keys())
        # || Example: "source_data.keys() = dict_keys(['1', '5'])"
        print('UTILS.PY - sup_dict | prodcuts queries: ', products)
        # || Example: "products = <QuerySet [<Product: carnosaurio>, <Product: hairy wings>]>

        for product in products:
            quantity = source_data.get(str(product.id), 0)
            subtotal = product.price * quantity
            seller_id = product.seller_id
            max_add_quantity = product.quantity - quantity

            if seller_id not in cart_items:
                cart_items[seller_id] = []

            cart_items[seller_id].append({
                'product': product,
                'quantity': quantity,
                'subtotal': subtotal,
                'max_add_quantity': max_add_quantity
            })

        print('UTILS.PY - sup_dict | cart_items: ', cart_items)

        # || Example: "cart_itmes = {
        #    <CustomUser: victorsup>: [
        #        {'product': <Product: carnosaurio>, 'quantity': 2, 'subtotal': Decimal('44.00'), 'max_add_quantity': 0}
        #    ],
        #    <CustomUser: nuevosupuser>: [
        #        {'product': <Product: hairy wings>, 'quantity': 1, 'subtotal': Decimal('88.00'), 'max_add_quantity': 8}
        #    ]
        # }"

    elif source == "order":  # Used for retrieval from DB
        # Process the data as an order, grouping by seller based on the database OrderItem records
        for item in source_data:  # Loop through each order item in the QuerySet
            product = item.product  # Retrieve the product associated with this order item
            quantity = item.quantity  # Get the quantity of this specific product in the order
            # Total price for this item (pre-calculated in the OrderItem model)
            subtotal = item.item_total
            seller_id = product.seller_id  # Identify the seller associated with the product

            if seller_id not in cart_items:  # Initialize a new entry for this seller if not present
                cart_items[seller_id] = []

            # Append product details to the corresponding seller's list
            cart_items[seller_id].append({
                'product': product,
                'quantity': quantity,
                'subtotal': subtotal,
            })

            # || Example (order scenario): "cart_items = {
            #    <CustomUser: victorsup>: [
            #        {'product': <Product: carnosaurio>, 'quantity': 2, 'subtotal': Decimal('44.00')}
            #    ],
            #    <CustomUser: nuevosupuser>: [
            #        {'product': <Product: hairy wings>, 'quantity': 1, 'subtotal': Decimal('88.00')}
            #    ]
            # }"

    print("------------------------------------------")
    return cart_items


def get_cart_items_count(request):
    """
    Calculates the total number of items in the shopping cart stored in the session.

    This function retrieves the shopping cart from the session and calculates
    the total quantity of items. It handles cases where the cart data might be 
    stored as integers or dictionaries for each product.

    Parameters:
    - request (HttpRequest): The request object containing the session data.

    Returns:
    - int: The total number of items in the shopping cart.
    """
    shopping_cart = request.session.get(
        'shopping_cart', {})  # Retrieve the cart from the session
    total_items = 0  # Initialize total items counter

    for product_id, details in shopping_cart.items():
        if isinstance(details, int):
            # If the item is stored as an integer, add it directly
            total_items += details
        elif isinstance(details, dict):
            # If the item is stored as a dictionary, extract the 'quantity'
            total_items += details.get('quantity', 0)
        else:
            # Optional: Handle unexpected formats for debugging purposes
            print(f"Unexpected format for product_id {product_id}: {details}")

    return total_items  # Return the total item count


def get_unread_messages_count(user):
    """
    Calculates the total number of unread messages for a user.

    This function queries the Message model to count all messages
    where the recipient is the given user and `is_read` is False.

    Parameters:
    - user (CustomUser): The currently authenticated user.

    Returns:
    - int: The total number of unread messages.
    """
    return Message.objects.filter(recipient=user, is_read=False).count()


def global_counts(request):
    """
    Adds global counts for new messages and cart items to the context.

    This function ensures that the count of unread messages and the total
    items in the shopping cart are always available in the context for 
    templates. These counts are only calculated if the user is authenticated.

    Parameters:
    - request (HttpRequest): The request object containing session and user data.

    Returns:
    - dict: A dictionary containing:
        - 'new_messages_count': The total number of unread messages.
        - 'cart_items_count': The total number of items in the cart.
    """
    if request.user.is_authenticated:
        # Calculate the number of unread messages
        new_messages_count = get_unread_messages_count(request.user)

        # Calculate the total number of items in the shopping cart
        cart_items_count = get_cart_items_count(request)

        return {
            'new_messages_count': new_messages_count,  # Total unread messages
            'cart_items_count': cart_items_count,  # Total items in the cart
        }

    # If the user is not authenticated, return zero counts
    return {
        'new_messages_count': 0,
        'cart_items_count': 0,
    }
