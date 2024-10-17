from django.contrib import admin

# Register your models here.

from .models import Product, Category, Subcategory


class ProductAdmin(admin.ModelAdmin):
    # Mostrar el ID y otros campos en la lista de objetos del admin
    list_display = ('id', 'name', 'price', 'seller_id',
                    'quantity', 'is_active', 'is_featured',
                    'is_bestseller', 'is_trending', 'rating')

    # Opcionalmente, puedes permitir hacer clic en el campo ID para editar el objeto
    list_display_links = ('id', 'name')


admin.site.register(Product, ProductAdmin)

admin.site.register(Category)

admin.site.register(Subcategory)
