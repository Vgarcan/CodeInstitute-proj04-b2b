from django.urls import path, include
from . import views

app_name = 'direct_messages'

urlpatterns = [
    path('', views.chat_view, name='chat'),
    path('<int:recipient_id>/', views.chat_view, name='chat'),
    path('send-message/<str:username>/',
         views.send_message, name='send_message'),
]
