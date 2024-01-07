from rest_framework import serializers
from cards.models import Category, Card

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name',)
