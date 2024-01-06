from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from accounts.models import User
from django.http import HttpResponse, HttpResponseRedirect


def user_register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['Create_password']
        confirmation = request.POST['Confirm_password']
        if confirmation!= password:
            return render(request, 'registration/register.html',{
                'password_message':'Passwords must match.'
            })

        else:
            user = User.objects.create_user(username,password)
            user.save()
            login(request, user)
            return redirect('accounts_web:register')

    else:
        return render(request, 'registration/register.html')