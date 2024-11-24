from django.urls import path, include
from . import views

app_name = 'users'

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/<int:user_id>', views.profile, name='user_profile'),
    path('profile', views.profile, name='user_profile'),
    path('edit_profile', views.edit_profile, name='edit_profile'),
    path('dashboard', views.dashboard, name='dashboard'),
]
