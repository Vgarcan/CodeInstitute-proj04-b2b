from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProductForm
from .models import Product, Category
from users.models import CustomUser
from django.contrib import messages
from users.decorators import role_required
from utils import sup_dict
from django.db.models import Q


# Create your views here.


@role_required("SUP")
def create_edit_product(request, prd_id=None):
    """
    View function to create or edit a product.

    This function allows users with the 'SUP' role to either create a new product
    or edit an existing one based on the provided product ID.

    Args:
        request: The HTTP request object.
        prd_id (str, optional): The ID of the product to edit. If None, a new product
                                will be created.

    Returns:
        HttpResponse: Rendered template with the product form.
    """

    # Check if a product ID is provided; if so, attempt to retrieve the existing product.
    if prd_id:
        # Retrieve the product by ID or return 404.
        product = get_object_or_404(Product, pk=prd_id)
        # Check if the current user is the seller of the product. If not, display an error message and redirect to the 'create' page.
        if product.seller_id != request.user:
            messages.error(
                request, "You do not have permission to edit this product.")
            return redirect("products:create")
    else:
        # No product ID provided, so a new product will be created.
        product = None

    # Handle form submission for creating or updating a product.
    if request.method == "POST":
        # Bind the submitted data to the ProductForm. If editing, the existing product data will be used.
        product_form = ProductForm(
            request.POST, request.FILES, instance=product)

        # Validate the form data.
        if product_form.is_valid():
            try:
                # Save the product instance but do not commit to the database yet.
                product = product_form.save(commit=False)
                # Assign the current user as the seller of the product.
                product.seller_id = request.user
                product.save()  # Commit the product to the database.

                # Show a success message to the user.
                messages.success(
                    request, "Product created/updated successfully")

                # Redirect to the 'create' view to create another product.
                return redirect("products:create")
            except Exception as e:
                # If an error occurs, display an error message.
                messages.error(
                    request, f"Error creating/updating product: {str(e)}")
                # Redirect back to the create page on error.
                return redirect("products:create")

    else:
        # If the request is a GET, prepare the form for rendering.
        # Load the product data into the form if editing.
        product_form = ProductForm(instance=product)

    # Render the template with the product form.
    return render(
        request,
        "products/prod-creation.html",
        {"prod_form": product_form,
         'product': product},  # Pass the product form to the template.
    )


def view_products(request, provider_id=None):
    """
    Retrieve and display products from the database based on the provided provider ID.

    Parameters:
    request (HttpRequest): The HTTP request object.
    provider_id (int, optional): The ID of the seller. If not provided, all products will be retrieved.

    Returns:
    HttpResponse: Rendered template with the products. If an error occurs, an error message will be displayed.
    """

    if provider_id is None:
        # Fetch all products from the database.
        products = Product.objects.all()
    else:
        # Fetch products from the database where the seller's ID matches the provided ID.
        try:
            # Check if the provided provider ID exists. If not, display an error message and redirect to the product list page.
            if CustomUser.objects.get(id=provider_id).role != "SUP":
                messages.error(request, "Invalid provider ID")
                products = {}  # Creates an EMPTY value
                return redirect("products:list")

            else:
                products = Product.objects.filter(seller_id=provider_id)
        except Exception as e:
            # Recognise the error and return the response as a message
            messages.error(request, "No product found")
            messages.warning(request, f'ERROR: "{e.__class__.__name__}": {e}')
            products = {}  # Creates an EMPTY value

    # Get the current user's shopping cart from the session.
    # If the 'shopping_cart' key does not exist in the session, use an empty dictionary as the default value.
    shopping_cart = request.session.get('shopping_cart', {})
    total_cost = request.session.get('cart_total', 0)

    # Retrieve the products from the shopping cart based on their IDs.
    # Use Django's filter function to retrieve the products with IDs present in the shopping cart.
    products_in_cart = Product.objects.filter(id__in=shopping_cart.keys())

    # Prepare a dictionary to group products by seller_id
    # imported from UTILS.PY
    cart_items = sup_dict(shopping_cart, source="cart")

    # Render the template with the products.
    return render(request,
                  "products/product-list.html",
                  {
                      "products": products,
                      'cart_items': cart_items,
                      'total_cost': total_cost
                  }
                  )


@role_required("SUP")
def delete_product(request, prd_id):
    """
    Deletes a product from the database based on the provided product ID.

    Parameters:
    request (HttpRequest): The HTTP request object.
    prd_id (int): The ID of the product to be deleted.

    Returns:
    HttpResponseRedirect: Redirects to the product list page after successful deletion.
                        Displays an error message if the user does not have permission to delete the product.
    """
    # Retrieve the product by ID or return 404.
    product = get_object_or_404(Product, pk=prd_id)
    # Check if the current user is the seller of the product. If not, display an error message and redirect to the product list page.
    if product.seller_id != request.user:
        messages.error(
            request, "You do not have permission to delete this product.")
        return redirect("users:dashboard")
    # Delete the product from the database.
    product.delete()
    # Show a success message to the user.
    messages.success(request, "Product deleted successfully")
    # Redirect to the product list page.
    return redirect("users:dashboard")


def view_product_detail(request, prd_id):
    """
    Retrieve and display the details of a product from the database based on the provided product ID.

    Parameters:
    request (HttpRequest): The HTTP request object.
    prd_id (int): The ID of the product to retrieve.

    Returns:
    HttpResponse: Rendered template with the product details. If the product with the given ID is not found, a 404 error page will be displayed.
    """
    # Retrieve the product by ID or return 404.
    product = get_object_or_404(Product, pk=prd_id)
    # Render the template with the product details.
    return render(request, "products/product-detail.html", {"product": product})


def search_products(request):
    """
    Searches products based on the search query, which includes products by name
    or products belonging to a category or its subcategories.

    Parameters:
    request (HttpRequest): The HTTP request object. This object contains information about the client's request.

    Returns:
    HttpResponse: Rendered template with the search results. If the search query is empty, an empty list of products is returned.
    """
    # Retrieve the query parameters
    query = request.GET.get("q", "").strip().lower()
    print(f"Search query: '{query}'")

    products = []  # Initialize the list of products

    if query:
        # # Checks for main Categories that matches the query
        matching_categories = Category.objects.filter(name__icontains=query)
        #! ### TEST ###
        print(matching_categories)
        #! ### TEST ###

        # # Gets the ID of all related Categories and Sub-Categories
        category_ids = set()
        for category in matching_categories:
            category_ids.add(category.id)  # Include the primary category
            # ? https://django-mptt.readthedocs.io/en/latest/mptt.models.html#mptt.models.MPTTModel.get_descendants
            category_ids.update(category.get_descendants(include_self=True).values_list(
                'id', flat=True))  # Include the secondary category

            #! ### TEST ###
            print(category_ids)
            #! ### TEST ###

        # search for Products that are related to the Category/Sub-Category or matches the name
        products = Product.objects.filter(
            Q(name__icontains=query) | Q(category_id__in=category_ids)
        )

        #! ### TEST ###
        print(f"Products found: {products.count()}")
        for product in products:
            print(f" - {product.name} (Category: {product.category_id.name})")
        #! ### TEST ###

    # Get the current user's shopping cart from the session.
    # If the 'shopping_cart' key does not exist in the session, use an empty dictionary as the default value.
    shopping_cart = request.session.get('shopping_cart', {})
    total_cost = request.session.get('cart_total', 0)

    # Retrieve the products from the shopping cart based on their IDs.
    # Use Django's filter function to retrieve the products with IDs present in the shopping cart.
    products_in_cart = Product.objects.filter(id__in=shopping_cart.keys())

    # Prepare a dictionary to group products by seller_id
    # imported from UTILS.PY
    cart_items = sup_dict(shopping_cart, source="cart")

    # Render the template with the products.
    return render(request,
                  "products/product-list.html",
                  {
                      "products": products,
                      'cart_items': cart_items,
                      'total_cost': total_cost
                  }
                  )


@role_required("BUY")
def add_product(request, prd_id, quantity):
    """
    Add a specified quantity of a product to a user's shopping cart using the session.

    Parameters:
    request (HttpRequest): The HTTP request object.
    prd_id (int): The ID of the product to add.
    quantity (int): The quantity of the product to add.

    Returns:
    HttpResponseRedirect: Redirects to the product detail page after successful addition to the shopping cart.
                        Displays an error message if the user does not have enough stock.
    """
    # Retrieve the product by ID or return 404.
    product = get_object_or_404(Product, pk=prd_id)
    product_qnt = product.quantity

    # Check if the user has enough stock to add the specified quantity of the product.
    if product_qnt < quantity:
        messages.error(request, "Insufficient stock")
        return redirect("products:item-view", prd_id=prd_id)

    # Get the current user's shopping cart from the session.
    if "shopping_cart" not in request.session:
        request.session["shopping_cart"] = {}

    # Update the shopping cart with the added product.
    # If the product already exists in the shopping cart, increment the quantity.
    if prd_id in request.session["shopping_cart"]:
        # Checks if the is enough to add the product
        total_in_cart = request.session["shopping_cart"][prd_id]
        to_add = total_in_cart + quantity
        if to_add <= product_qnt:
            request.session["shopping_cart"][prd_id] += quantity
        else:
            messages.error(request, "No more available products")
            # Redirect to the product detail page.
            return redirect("products:item-view", prd_id=prd_id)

    # If product not in the shopping cart, creates a new one
    else:
        request.session["shopping_cart"][prd_id] = quantity

    # Update the total price in the shopping cart session.
    request.session["cart_total"] = float(
        sum(
            Product.objects.get(pk=product).price * quantity
            for product, quantity in request.session["shopping_cart"].items()
        )
    )

    # Show a success message to the user.
    messages.success(request, f"Product added to cart: {product.name}")

    # Redirect to the product detail page.
    return redirect("products:item-view", prd_id=prd_id)


@role_required('BUY')
def view_shopping_cart(request):
    """
    Retrieve and display the items in the user's shopping cart.

    Parameters:
    request (HttpRequest): The HTTP request object. This object contains information about the client's request, including session data.

    Returns:
    HttpResponse: Rendered template with the shopping cart items. The template displays the products in the user's cart along with their total cost.
    """
    # Get the current user's shopping cart from the session.
    # If the 'shopping_cart' key does not exist in the session, use an empty dictionary as the default value.
    shopping_cart = request.session.get('shopping_cart', {})
    total_cost = request.session.get('cart_total', 0)

    # Retrieve the products from the shopping cart based on their IDs.
    # Use Django's filter function to retrieve the products with IDs present in the shopping cart.
    products = Product.objects.filter(id__in=shopping_cart.keys())

    # Prepare a dictionary to group products by seller_id
    # imported from UTILS.PY
    cart_items = sup_dict(shopping_cart, source="cart")

    # Render the template with the shopping cart items.
    # Pass the products and total cost as context variables to the template.
    return render(request, 'products/shopping-cart.html', {
        'cart_items': cart_items,
        'total_cost': total_cost
    })


@role_required('BUY')
def remove_product(request, prd_id, quantity):
    """
    Remove a specific quantity of a product from the user's shopping cart based on the provided product ID.

    Parameters:
    request (HttpRequest): The HTTP request object.
    prd_id (int): The ID of the product to remove.
    quantity (int): The quantity to remove from the cart.

    Returns:
    HttpResponseRedirect: Redirects to the shopping cart page after successful removal.
    """
    # Get the current user's shopping cart from the session.
    shopping_cart = request.session.get('shopping_cart', {})

    # Check if the product exists in the cart
    if prd_id in shopping_cart:
        current_quantity = shopping_cart[prd_id]

        # If the selected quantity is greater than or equal to the current quantity, remove the product
        if quantity >= current_quantity:
            del shopping_cart[prd_id]
            messages.success(
                request,
                f'Removed {current_quantity} of {Product.objects.get(
                    id=prd_id).name} from the cart.'
            )
        else:
            # Otherwise, reduce the quantity
            shopping_cart[prd_id] -= quantity
            messages.success(
                request,
                f'Removed {quantity} of {Product.objects.get(
                    id=prd_id).name} from the cart.'
            )

    # Update the shopping cart in the session
    request.session['shopping_cart'] = shopping_cart

    # Redirect to the shopping cart page
    return redirect('products:view-cart')


@role_required('BUY')
def checkout(request):
    """
    This function processes the user's checkout request and redirects them to the payment gateway.
    Parameters:
    request (HttpRequest): The HTTP request object. This object contains information about the client's request, including session data.
    Returns:
    HttpResponseRedirect: Redirects the user to the payment gateway.
    """
    # Get the current user's shopping cart from the session.
    shopping_cart = request.session.get('shopping_cart', {})
    total_cost = request.session.get('cart_total', 0)

    # If the shopping cart is empty, redirect the user to the product list
    if not shopping_cart:
        messages.error(request, 'Your shopping cart is empty.')
        return redirect('products:list')

    # If the total cost is zero, redirect the user to the product list
    if total_cost == 0:
        messages.error(
            request, 'Your shopping cart does not contain any items.')
        return redirect('products:list')

    # Redirect the user to the payment gateway
    return redirect('payments:process-payment', total_cost)
