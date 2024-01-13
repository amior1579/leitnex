from django.shortcuts import render
from boxes.serializers import BoxSerializer
from cards.serializers import CardSerializer, CategorySerializer
from boxes.models import Box, Partition, Section
from cards.models import Category,Card
from django.shortcuts import get_object_or_404
import django.utils.timezone
from datetime import datetime 
from boxes.learn_days import *
from boxes.card_guess import *


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



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def start_learning(request):
    auth_user = request.user

    if request.method == 'POST':
        box_id = request.GET.get('box_id')
        Q_box = Box.objects.get(id=box_id, user=auth_user)
        start_learn_time = Q_box.start_time
        learn_days = Q_box.learn_days

        if start_learn_time is None:
            Q_box.start_time = datetime.now()
            Q_box.save()
            print(Q_box)  

        day_functions = [day_1]
        learn_cards = day_functions[learn_days](Q_box)

        serializer = CardSerializer(learn_cards, many=True)


        # print(learn_cards)

    return Response(serializer.data, status=status.HTTP_200_OK)



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def card_guess(request):
    auth_user = request.user

    if request.method == 'POST':
        box_id = request.GET.get('box_id')
        card_id = request.GET.get('card_id')
        guess = request.GET.get('guess')

        Q_box = Box.objects.get(id=box_id, user=auth_user)
        learn_days = Q_box.learn_days
        # print(card_id)

        desired_card = None
        for card in Q_box.card_box.all():
            # print(card)
            if card.id == int(card_id):
                desired_card = card
                break

        # print(desired_card)
    

        day_functions = ["",guess_day_1]
        card_guess = day_functions[learn_days](Q_box,desired_card,guess)

    # return Response(serializer.data, status=status.HTTP_200_OK)
    return Response({'message': 'Done'}, status=status.HTTP_201_CREATED)






