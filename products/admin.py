from django.contrib import admin
from mptt.admin import MPTTModelAdmin

# Register your models here.

from .models import Product, Category, OrderProductSnapshot


class ProductAdmin(admin.ModelAdmin):
    # Mostrar el ID y otros campos en la lista de objetos del admin
    list_display = (
        "id",
        "name",
        "price",
        "seller_id",
        "quantity",
        "is_active",
        "is_featured",
        "is_bestseller",
        "is_trending",
        "rating",
    )

    # Opcionalmente, puedes permitir hacer clic en el campo ID para editar el objeto
    list_display_links = ("id", "name")


admin.site.register(Product, ProductAdmin)


# Customize the admin interface for the Category model


class CategoryAdmin(MPTTModelAdmin):
    mptt_level_indent = 30
    list_display = ("name",)
    list_display_links = ("name",)
    search_fields = ("name",)


admin.site.register(Category, CategoryAdmin)


class OrderProductSnapshotAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "price", "category", "created_on")
    list_display_links = ("id", "name")
    search_fields = ("id", "name", "price", "category", "created_on")

    # Navigation filters
    list_filter = ("id", "created_on")
    # READ ONLY fields
    readonly_fields = (
        "id",
        "name",
        "price",
        "category",
        "created_on",
        "description",
        "image",
    )


admin.site.register(OrderProductSnapshot, OrderProductSnapshotAdmin)
