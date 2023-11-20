from django.db import models


def initialize_message_received_time():
    return None

class Message(models.Model):
    '''
    A model for a message
    '''
    MESSAGE_STATUS = (
        ('QUEUED', 'queued'),
        ('SENT', 'sent')
    )
    sender = models.CharField(max_length=50, null=False)# change this to be a user foreignkey field
    receiver = models.CharField(max_length=50, null=False)#user foreign key
    message_body = models.CharField(max_length=300, null=False)#decide on message length
    status = models.CharField(max_length=20, choices=MESSAGE_STATUS, default='QUEUED', db_index=True)
    sent_at = models.DateTimeField(auto_now_add=True)
    received_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return f"message: {self.sender} to {self.receiver}"