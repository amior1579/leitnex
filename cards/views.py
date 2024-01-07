from django.shortcuts import render
from cards.serializers import CategorySerializer
from cards.models import Category, Card

# rest framework
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view , permission_classes ,authentication_classes
from rest_framework.permissions import IsAuthenticated



@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def get_or_create_category(request):
    auth_user = request.user
    if request.method == 'GET':
        q_Category = Category.objects.filter(user=auth_user)
        serializer = CategorySerializer(q_Category,many=True)
        # print(serializer)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

    if request.method == 'POST':
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['user'] = auth_user
            serializer.save()
            return Response({'message': 'Done', 'data':serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)