from django.urls import path, include
from . import views
from boxes import views

app_name = 'boxes_web'

urlpatterns = [
    path('getOrCreate_box/', views.get_or_create_box, name='get_or_create_box'),

]