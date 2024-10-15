from allauth.account.forms import SignupForm
from django import forms
from .models import Product

# Define the custom form for user signup


class ProductForm(forms.ModelForm):
    """
    A form for creating and editing Product models.

    This form is used to create and edit product information, such as name, description, price, 
    quantity, and category. It is based on Django's ModelForm and is linked to the Product model.
    """

    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'quantity', 'category_id',
                  'subcategory_id', 'image']  # Fields that will appear in the form
