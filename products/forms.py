from django import forms
from .models import Product, Category

# Define the custom form for user signup


class ProductForm(forms.ModelForm):
    """
    A form for creating and editing Product models.

    This form is used to create and edit product information, such as name, description, price, 
    quantity, and category. It is based on Django's ModelForm and is linked to the Product model.
    """

    class Meta:
        """ Modify thr Product Form behavior. """
        model = Product
        fields = ['name', 'description', 'price', 'quantity', 'category_id',
                  'image']  # Fields that will appear in the form

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        # Filter categories that are not parent categories (i.e., subcategories only)
        # self.fields['category_id'].queryset = Category.objects.filter(
        #     parent__isnull=False).order_by('name')
        self.fields['category_id'].queryset = Category.objects.all()
