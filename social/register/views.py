from django.shortcuts import render, reverse
from .models import User
from django.http import HttpResponseRedirect
# Create your views here.


def register(request):
    return render(request, 'register/register.html')


def register_error(request, error):
    if error == 'InvalidUser':
        return render(request, 'register/register.html', {
            'error': True,
            'error_message': 'Username is already taken'
        })
    elif error == 'InvalidEmail':
        return render(request, 'register/register.html', {
            'error': True,
            'error_message': 'Email is already taken'
        })


def chk_username_taken(username):
    taken = False
    users = User.objects.all()
    for user in users:
        if user.user_name == username:
            taken = True
            break
    return taken


def chk_email_taken(email):
    taken = False
    users = User.objects.all()
    for user in users:
        if user.email == email:
            taken = True
            break
    return taken


def home(request):
    if request.method == 'POST':
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        user_name = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        if chk_username_taken(user_name):
            return HttpResponseRedirect(reverse('social:register_error', args=['InvalidUser']))
        elif chk_email_taken(email):
            return HttpResponseRedirect(reverse('social:register_error', args=['InvalidEmail']))
        else:
            new_user = User(first_name=first_name, last_name=last_name,
                            user_name=user_name, password=password, email=email)
            new_user.save()
            return render(request, 'register/home.html', {'user': new_user})

    elif request.method == 'GET':
        users = User.objects.all()
        user_name = request.GET['username']
        password = request.GET['password']
        active_user = None
        for user in users:
            if user.user_name == user_name:
                active_user = user
        if password == active_user.password:
            return render(request, 'register/home.html', {'user': active_user})
        else:
            return HttpResponseRedirect(reverse('login:login_error', args=['InvalidLogin']))

