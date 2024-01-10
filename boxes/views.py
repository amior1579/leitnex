from django.shortcuts import render
from boxes.serializers import BoxSerializer
from cards.serializers import CardSerializer, CategorySerializer
from boxes.models import Box, Partition, Section
from cards.models import Category,Card
from django.shortcuts import get_object_or_404

# rest framework
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view , permission_classes ,authentication_classes
from rest_framework.permissions import IsAuthenticated


@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def get_or_create_box(request):
    auth_user = request.user

    if request.method == 'POST':
        serializer = BoxSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['user'] = auth_user

            for i in range(1, 6):
                new_partitions = Partition.objects.create(name=f'partition-{i}')

                if i == 1:
                    new_section = Section.objects.create(name=f'section-{i}')
                    new_partitions.choise_section.add(new_section)
                elif i == 2:
                    for i in range(2, 4):
                        new_section = Section.objects.create(name=f'section-{i}')
                        new_partitions.choise_section.add(new_section)
                elif i == 3:
                    for i in range(4, 8):
                        new_section = Section.objects.create(name=f'section-{i}')
                        new_partitions.choise_section.add(new_section)
                elif i == 4:
                    for i in range(8, 16):
                        new_section = Section.objects.create(name=f'section-{i}')
                        new_partitions.choise_section.add(new_section)
                elif i == 5:
                    for i in range(16, 31):
                        new_section = Section.objects.create(name=f'section-{i}')
                        new_partitions.choise_section.add(new_section)

                serializer.validated_data['partitions'].append(new_partitions)

            serializer.save()
            return Response({'message': 'Done', 'data':serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def get_or_create_cardbox(request):
    auth_user = request.user
    box_id = request.GET.get('box_id')

    if request.method == 'GET':
        Q_box = get_object_or_404(Box, user=auth_user, id=box_id)

        print(Q_box.card_box)
        serializer = CardSerializer(Q_box.card_box, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    if request.method == 'POST':
        serializer = CardSerializer(data=request.data)

        if serializer.is_valid():
            serializer.validated_data['choice_user'] = auth_user

            new_card = serializer.save()

            add_to_box = Box.objects.get(id=box_id)
            add_to_box.card_box.add(new_card)

            serializer.save()
            return Response({'message': 'Done', 'data':serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_category_to_cards_box(request):
    auth_user = request.user

    if request.method == 'POST':
        category_id = request.GET.get('category_id')
        box_id = request.GET.get('box_id')

        box_instance = Box.objects.get(id=box_id, user=auth_user)
        category_instance = Card.objects.filter(choice_category=category_id, choice_user=auth_user)
        print(category_instance)

        box_instance.card_box.add(*category_instance)


    return Response({'message': 'Done'}, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)