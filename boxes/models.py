from django.db import models
from accounts.models import User
from cards.models import Card




class Section(models.Model):
    name = models.CharField(max_length=100)
    choise_cards = models.ManyToManyField(Card,blank=True,default=None,verbose_name='choise cards')

    def __str__(self):
        return f'{self.id},{self.name}'
    
    def save(self, *args, **kwargs):
        if not self.name:
            self.name = f'section-{self.pk}'
        super().save(*args, **kwargs)

    # def get_queryset(self, user):
    #     return self.choise_cards.filter(choice_user=user)

class Partition(models.Model):
    name = models.CharField(max_length=100)
    choise_section = models.ManyToManyField(Section,blank=True,default=None,verbose_name='choise section')

    def __str__(self):
        return f'{self.id},{self.name}'
    
    def save(self, *args, **kwargs):
        if not self.name:
            self.name = f'partition-{self.pk}'
        super().save(*args, **kwargs)



class Box(models.Model):
    user = models.ForeignKey(User,blank=True, null=True, on_delete=models.CASCADE)
    box_name = models.CharField(max_length=100, blank=False, null=False, verbose_name='box name')
    partitions = models.ManyToManyField(Partition,blank=True,default=None,verbose_name='partitions')
    card_box = models.ManyToManyField(Card,blank=True,default=None,verbose_name='card box')
    start_time = models.DateField(blank=True,null=True, verbose_name='start time')
    learn_days = models.IntegerField(blank=True,null=True, verbose_name='learn_days')

    def __str__(self):
        return f'{self.id},{self.box_name}'