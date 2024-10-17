from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProductForm
from .models import Product
from django.contrib import messages
from users.decorators import role_required

# Create your views here.


@role_required('SUP')
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
                request, 'You do not have permission to edit this product.')
            return redirect('products:create')
    else:
        # No product ID provided, so a new product will be created.
        product = None

    # Handle form submission for creating or updating a product.
    if request.method == 'POST':
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
                    request, 'Product created/updated successfully')

                # Redirect to the 'create' view to create another product.
                return redirect('products:create')
            except Exception as e:
                # If an error occurs, display an error message.
                messages.error(
                    request, f'Error creating/updating product: {str(e)}')
                # Redirect back to the create page on error.
                return redirect('products:create')

    else:
        # If the request is a GET, prepare the form for rendering.
        # Load the product data into the form if editing.
        product_form = ProductForm(instance=product)

    # Render the template with the product form.
    return render(request, 'products/prod-creation.html', {
        'prod_form': product_form  # Pass the product form to the template.
    })
