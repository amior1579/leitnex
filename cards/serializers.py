from rest_framework import serializers
from cards.models import Category, Card

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id','user','category_name',)


class CardSerializer(serializers.ModelSerializer):
    choice_category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), required=False, )

    class Meta:
        model = Card
        fields = ('id','question','answer','image','choice_category','choice_user')


    # def create(self, validated_data):
    #     choice_category_name = validated_data.pop('choice_category')
    #     category, _ = Category.objects.get_or_create(name=category_name, user=self.context['request'].user)
    #     validated_data['category'] = category
    #     return Card.objects.create(**validated_data)