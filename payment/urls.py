from django.urls import path
from . import views

app_name = "payment"

urlpatterns = [
    path("process-payment/", views.checkout, name="user_information"),
    path("success/", views.payment_success, name="payment_success"),
]
