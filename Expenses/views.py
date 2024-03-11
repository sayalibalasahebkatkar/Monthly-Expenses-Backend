from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Item
from .serializer import ItemSerializer
from rest_framework import serializers
from rest_framework import status

@api_view(['POST'])
def add_item(request):
    data = ItemSerializer(data=request.data)
    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
