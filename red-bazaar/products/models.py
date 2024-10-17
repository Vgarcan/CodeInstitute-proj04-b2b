from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.utils.text import slugify

# Create your models here.


class Category(MPTTModel):
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
        # Automatically generate the slug based on the product title
        self.slug = slugify(f"{self.seller_id}-{self.name}")
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.name}"


### WEBSITES: ###
    # Categories and subCategories : https://stackoverflow.com/questions/60120266/django-categories-and-subcategories
#################
