from django.urls import path, include
from . import views
from accounts import views

app_name = 'accounts_web'

urlpatterns = [
    # path('register_form/', views.user_register_form, name='register'),
    path('register/', views.user_register, name='register'),
    path('login/', views.user_login, name='login'),
    # path('logout/', views.LogoutView.as_view(), name='logout'),
    path('profile/', views.user_profile, name="profile"),
    path('profile/cards', views.user_cards, name="cards"),

]