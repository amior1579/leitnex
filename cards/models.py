from django.db import models
from accounts.models import User

class Category(models.Model):
    user = models.ForeignKey(User,blank=True, null=True, on_delete=models.CASCADE)
    category_name = models.CharField(max_length=100, blank=False, null=False, verbose_name='categoryـname')

    def __str__(self):
        return f'{self.id},{self.category_name}'


class Card(models.Model):
    question = models.CharField(max_length=500, blank=False, null=False, verbose_name='question')
    answer = models.CharField(max_length=500,blank=False, null=False, verbose_name='answer')
    image = models.ImageField(default=None, null=True, blank=True, upload_to="media", verbose_name='avatar')
    choice_category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='cards', verbose_name='choice_category')
    choice_user = models.ForeignKey(User,blank=True, null=True, on_delete=models.CASCADE)


    def __str__(self):
        return f'{self.question}'
    
    @classmethod
    def get_cards_by_category_name(cls, category_name, user):
        category = Category.objects.get(category_name=category_name, user=user)
        return cls.objects.filter(choice_category=category, user=user)
