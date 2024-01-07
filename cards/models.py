from django.db import models
from accounts.models import User

class Category(models.Model):
    user = models.ForeignKey(User,blank=True, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=False, null=False, verbose_name='category name')


class Card(models.Model):
    question = models.CharField(max_length=500, blank=False, null=False, verbose_name='question')
    answer = models.CharField(max_length=500,blank=False, null=False, verbose_name='answer')
    image = models.ImageField(default=None, null=True, blank=True, upload_to="media", verbose_name='avatar')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='cards', verbose_name='category')
