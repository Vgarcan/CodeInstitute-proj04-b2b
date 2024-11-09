from django.urls import path, include
from . import views

app_name = 'orders'

urlpatterns = [

    path('place-order', views.create_order, name='place_order'),
    path('order-details/<str:order_id>',
         views.order_detail, name='order_details'),
    path('sup-order-details/<str:order_id>',
         views.supplier_order_detail, name='sup_order_details'),
    path('order-confirmation', views.confirm_order, name='confirmation'),
    path('update-order-status/<str:order_id>/<str:order_status>',
         views.update_order, name='update_order'),

]
