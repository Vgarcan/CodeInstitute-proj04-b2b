from django.urls import path, include
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('not-available/', views.under_dev, name='not_available'),
    path('contact/', views.contact, name='contact'),
    path('faq/', views.faq, name='faq'),
    path('pricing/', views.pricing, name='pricing'),
    path('terms/', views.terms, name='terms'),
    path('privacy-policy/', views.priv_pol, name='privpol'),
]
