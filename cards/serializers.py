from rest_framework import serializers
from cards.models import Category, Card

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('user','category_name',)

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ('question','answer','image','choice_category','choice_user')
