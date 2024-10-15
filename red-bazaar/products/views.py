from django.shortcuts import render, redirect
from .forms import ProductForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from users.decorators import role_required

# Create your views here.


@role_required('SUP')
def create_product(request):

    if request.method == 'POST':
        product_form = ProductForm(request.POST, request.FILES)
        if product_form.is_valid():
            try:
                # Save the product with the current user as the seller
                # commit FALSE to only instanciate the product
                product = product_form.save(commit=False)
                product.seller_id = request.user
                # Save the product
                product.save()
                messages.success(request, 'Product created successfully')
                return redirect('products:create')
            except Exception as e:
                messages.error(request, f'Error creating product: {str(e)}')
                return redirect('products:create')

    else:
        product_form = ProductForm()

    return render(request, 'products/prod-creation.html', {
        'prod_form': product_form
    })
