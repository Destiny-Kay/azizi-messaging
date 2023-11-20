from django.shortcuts import render
from django.db import transaction
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response


from message_handler.models import Message
from message_handler.serializers import MessageSerializer


class QueueMessageView(APIView):
    '''
    An endpoint that queues messages in a database
    '''
    def post(self, request, *args, **kwargs):
        
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SendQueuedMessageView(APIView):
    '''
    An API endpoint for querying and sending queued messages
    '''
    def get(self, request, *args, **kwargs):
        try:
            queued_messages = Message.objects.filter(status='QUEUED')
        except Message.DoesNotExist:
            return Response({
                'message': 'No messages in queue'
            }, status=status.HTTP_404_NOT_FOUND)

        #forwading logic might want to use a message queue
        for message in queued_messages:
            #Add the forward logic.. send message api
            message.status = 'SENT'
        with transaction.atomic():
            Message.objects.bulk_update(queued_messages, ['status'])
        serializer = MessageSerializer(queued_messages, many=True)
            
        return Response(serializer.data, status.HTTP_200_OK)