from django.urls import path
from message_handler.views import SendQueuedMessageView, QueueMessageView


urlpatterns = [
    path('queue-message/', QueueMessageView.as_view(), name='queue-message'),
    path('send-message/', SendQueuedMessageView.as_view(), name='send-message')
]