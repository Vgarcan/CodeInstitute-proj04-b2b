from django.contrib import admin
from .models import Order, OrderItem, ShipAddr


class OrderItemAdmin(admin.TabularInline):
    model = OrderItem
    extra = 0  # No extra empty forms
    max_num = 0  # Max number of items
    can_add = False  # No ability to add new order items through admin interface
    can_delete = False  # No ability to delete order items through admin interface

    # READ ONLY fields
    readonly_fields = ('product', 'quantity', 'item_total')

    # Display fields
    fields = ('product', 'quantity', 'item_total')


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'buyer', 'seller', 'status', 'ordered_on')
    list_display_links = ('id', )
    inlines = [OrderItemAdmin]  # Adds OrderItem

    # Navigation filters
    list_filter = ('status', 'ordered_on')
    search_fields = ('buyer__username', 'seller__username', 'id')

    # READ ONLY fields
    readonly_fields = ('buyer', 'seller', 'total_price',
                       'ordered_on', 'status')


admin.site.register(Order, OrderAdmin)


class ShipAddrAdmin(admin.ModelAdmin):
    list_display = ('id', 'username')
    list_display_links = ('id', 'username')


admin.site.register(ShipAddr, ShipAddrAdmin)
