from django.shortcuts import render
from boxes.serializers import BoxSerializer
from boxes.models import Box, Partition, Section
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