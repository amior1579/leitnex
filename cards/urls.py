from django.urls import path, include
from . import views
from cards import views

app_name = 'cards_web'

urlpatterns = [
    path('getOrCreate_category/', views.get_or_create_category, name='get_or_create_category'),

]