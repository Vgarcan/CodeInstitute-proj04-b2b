from django.urls import path, include
from . import views

app_name = 'products'

urlpatterns = [

    path('create', views.create_product, name='create'),

]
