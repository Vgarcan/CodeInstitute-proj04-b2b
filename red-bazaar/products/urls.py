from django.urls import path, include
from . import views

app_name = 'products'

urlpatterns = [

    path('create/<str:prd_id>', views.create_edit_product, name='create'),
    path('create', views.create_edit_product, name='create'),

]
