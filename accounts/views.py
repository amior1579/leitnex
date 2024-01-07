from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from accounts.models import User
from django.http import HttpResponse, HttpResponseRedirect


def user_register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['create_password']
        confirmation = request.POST['confirm_password']
        if confirmation!= password:
            return render(request, 'registration/register.html',{
                'password_message':'Passwords must match.'
            })

        else:
            user = User.objects.create_user(username,password)
            user.set_password(password)
            user.save()
            login(request, user)
            return redirect('home')

    else:
        return render(request, 'registration/register.html')
    


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'registration/login.html',{
                'message': 'Invalid username and/or password.',
            })

    else:
        return render(request, 'registration/login.html')
    

def user_profile(request):
    return render(request, 'registration/profile.html')


def user_cards(request):
    return render(request, 'registration/cards.html')