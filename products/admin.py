from django.contrib import admin
from mptt.admin import MPTTModelAdmin

# Register your models here.

from .models import Product, Category


class ProductAdmin(admin.ModelAdmin):
    # Mostrar el ID y otros campos en la lista de objetos del admin
    list_display = ('id', 'name', 'price', 'seller_id',
                    'quantity', 'is_active', 'is_featured',
                    'is_bestseller', 'is_trending', 'rating')

    # Opcionalmente, puedes permitir hacer clic en el campo ID para editar el objeto
    list_display_links = ('id', 'name')


admin.site.register(Product, ProductAdmin)


# Customize the admin interface for the Category model

class CategoryAdmin(MPTTModelAdmin):
    mptt_level_indent = 30
    list_display = ('name',)
    list_display_links = ('name',)
    search_fields = ('name',)


admin.site.register(Category, CategoryAdmin)
