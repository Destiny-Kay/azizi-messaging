from message_handler.models import Message
from rest_framework.serializers import ModelSerializer


class MessageSerializer(ModelSerializer):
    '''
    A serializer for the message model
    '''
    class Meta:
        model = Message
        fields = '__all__'

