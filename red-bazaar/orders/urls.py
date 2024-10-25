from django.urls import path, include
from . import views

app_name = 'orders'

urlpatterns = [

    path('place-order', views.create_order, name='place_order'),
    path('order-confirmation', views.confirm_order, name='confirmation'),

]
