from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.utils.text import slugify

# Create your models here.


class Category(MPTTModel):
    """
    Represents a category in a hierarchical structure using the MPTT (Modified Preorder Tree Traversal) model.

    Attributes:
        name (str): The name of the category, limited to 250 characters.
        slug (str): A unique slug for each category/subcategory, automatically generated from the name.
        description (str): An optional description of the category, limited to 250 characters.
        parent (TreeForeignKey): A reference to the parent category, allowing the creation of a parent-child relationship. 
                                 If the parent category is deleted, its children are also deleted.

    MPTTMeta:
        order_insertion_by (list): Defines the order in which categories are inserted into the hierarchy, sorted by name.

    Meta:
        unique_together (tuple): Ensures the uniqueness of the slug within the same parent category.
        verbose_name_plural (str): The plural form used in the admin interface for the model.
    """
    name = models.CharField(max_length=250)
    # Unique slug for each category/subcategory
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField(max_length=250, blank=True, null=True)
    parent = TreeForeignKey(
        # Reference to the same model to create hierarchy (parent-child)
        'self',
        blank=True,
        null=True,
        related_name='children',  # Access subcategories from a category
        # If a parent category is deleted, its children are also deleted
        on_delete=models.CASCADE
    )

    class MPTTMeta:  # Esta clase es importante para configurar el modelo MPTT
        # Esto organiza las categorías por nombre
        order_insertion_by = ['name']

    class Meta:
        # Ensure uniqueness of the slug within the same parent
        unique_together = ('slug', 'parent',)
        verbose_name_plural = "categories"  # Plural form for admin interface

    def save(self, *args, **kwargs):
        """
        Overriding the save method to automatically set the name to lowercase.
        """
        self.name = self.name.lower()
        # Automatically generate the slug based on the Category title
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        full_path = [self.name]  # Start with the current category's name
        parent = self.parent
        # Build the full path by iterating over the parent hierarchy
        while parent is not None:
            full_path.append(parent.name)
            parent = parent.parent
        # Return the full path in reverse order (root -> current)
        return ' -> '.join(full_path[::-1])


class Product(models.Model):
    """
    Represents a product sold by a seller in the system.

    Attributes:
        seller_id (ForeignKey): A reference to the CustomUser model, representing the seller of the product.
        slug (str): A unique slug for URL identification, automatically generated from the seller and product name.
        category_id (ForeignKey): A reference to the Category model, linking the product to its category.
        name (str): The name of the product, limited to 250 characters.
        price (Decimal): The price of the product, with a maximum of 4 digits and 2 decimal places.
        quantity (int): The available quantity of the product, defaulting to 0.
        description (str): An optional description of the product, limited to 250 characters.
        image (ImageField): An optional image of the product, uploaded to the 'products/' directory.
        created_at (DateTimeField): The timestamp when the product was created, set automatically.
        updated_at (DateTimeField): The timestamp when the product was last updated, set automatically.
        is_active (bool): A flag indicating if the product is active (available for sale), defaulting to True.
        is_featured (bool): A flag indicating if the product is featured, defaulting to False.
        is_bestseller (bool): A flag indicating if the product is a bestseller, defaulting to False.
        is_trending (bool): A flag indicating if the product is trending, defaulting to False.
        rating (int): The rating of the product, defaulting to 0.
    """

    seller_id = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE)
    # Slug for URL identification, unique
    slug = models.SlugField(unique=True, blank=True)
    category_id = models.ForeignKey(
        Category,
        related_name="products",  # Allows reverse access from Category to Product
        on_delete=models.CASCADE)
    name = models.CharField(max_length=250, blank=True, null=True)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    quantity = models.IntegerField(default=0)
    description = models.TextField(max_length=250, blank=True, null=True)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)
    is_bestseller = models.BooleanField(default=False)
    is_trending = models.BooleanField(default=False)
    rating = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        """
        Overriding the save method to automatically generate a unique slug for the product.

        Parameters:
        *args: Variable length argument list. Passed to the superclass's save method.
        **kwargs: Arbitrary keyword arguments. Passed to the superclass's save method.

        Returns:
        None. The method modifies the instance's slug attribute and calls the superclass's save method.
        """
        # Automatically generate the slug based on the product title
        self.slug = slugify(f"{self.seller_id}-{self.name}")
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.name}"


### WEBSITES: ###
    # Categories and subCategories : https://stackoverflow.com/questions/60120266/django-categories-and-subcategories
#################
