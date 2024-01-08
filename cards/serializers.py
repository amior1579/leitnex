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


    # def create(self, validated_data):
    #     choice_category_name = validated_data.pop('choice_category')
    #     category, _ = Category.objects.get_or_create(name=category_name, user=self.context['request'].user)
    #     validated_data['category'] = category
    #     return Card.objects.create(**validated_data)