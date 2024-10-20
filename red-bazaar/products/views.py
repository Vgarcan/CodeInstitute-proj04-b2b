from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProductForm
from .models import Product
from users.models import CustomUser
from django.contrib import messages
from users.decorators import role_required

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
        {"prod_form": product_form},  # Pass the product form to the template.
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

    # Render the template with the products.
    return render(request, "products/product-list.html", {"products": products})


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
        return redirect("products:list")
    # Delete the product from the database.
    product.delete()
    # Show a success message to the user.
    messages.success(request, "Product deleted successfully")
    # Redirect to the product list page.
    return redirect("products:list")


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
    This function retrieves products from the database based on the provided
    search query and renders them in a template.
    """
    # Retrieve the search query from the request.
    query = request.GET.get("search")
    # Filter the products based on the search query.
    products = Product.objects.filter(name__icontains=query)
    # Render the template with the filtered products.
    return render(request, "products/product-list.html", {"products": products})


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
    if prd_id in request.session["shopping_cart"]:
        request.session["shopping_cart"][prd_id] += quantity
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
