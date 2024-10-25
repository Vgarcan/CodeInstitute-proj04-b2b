from django.contrib import admin

from .models import *

# Register your models here.


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'buyer', 'seller', 'status', 'ordered_on')
    list_display_links = ('id', )


class OrderItemsAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'product', 'quantity', 'item_total')
    list_display_links = ('id', 'order', )


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemsAdmin)
