from rest_framework import serializers
from boxes.models import Box

class BoxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Box
        fields = ('id','user','box_name','partitions',)

