from django.urls import path, include
from . import views
from boxes import views

app_name = 'boxes_web'

urlpatterns = [
    path('getOrCreate_box/', views.get_or_create_box, name='get_or_create_box'),
    path('getOrCreate_cardbox/', views.get_or_create_cardbox, name='get_or_create_cardbox'),
    path('addCategoryToCardsBox/', views.add_category_to_cards_box, name='add_category_to_cards_box'),
    path('startLearning/', views.start_learning, name='start_learning'),
    path('cardGuess/', views.card_guess, name='card_guess'),

]