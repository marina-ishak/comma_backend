# chatbot/urls.py
from django.urls import path
from .views import ChatMessageListCreateView

urlpatterns = [
    path('chat/', ChatMessageListCreateView.as_view(), name='chat-list-create'),
]
