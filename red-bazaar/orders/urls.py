from django.urls import path, include
from . import views

app_name = 'orders'

urlpatterns = [

    path('place-order', views.create_order, name='place_order'),
    path('order-details/<str:order_id>',
         views.order_detail, name='order_details'),
    path('order-confirmation', views.confirm_order, name='confirmation'),
    path('update-order-status/<str:order_id>',
         views.update_order, name='update_order'),

]
