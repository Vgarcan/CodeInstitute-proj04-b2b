from django.urls import path, include
from . import views

app_name = 'products'

urlpatterns = [

    path('create/<str:prd_id>', views.create_edit_product, name='create'),
    path('create', views.create_edit_product, name='create'),
    path('products-list/<str:provider_id>', views.view_products, name='all'),
    path('products-list', views.view_products, name='all'),
    path('delete-product', views.delete_product, name='delete'),
    path('details/<int:prd_id>', views.view_product_detail, name='item-view'),
    path('search', views.search_products, name='search'),
    path('add-to-cart/<str:prd_id>/<int:quantity>',
         views.add_product, name='add-cart'),

]
