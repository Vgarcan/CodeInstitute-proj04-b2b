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


def calculate_total_from_sups():
    pass
