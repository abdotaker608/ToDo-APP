from django.shortcuts import render

# Create your views here.


def login(request):
    return render(request, 'login/login.html')


def login_error(request, login_error_404):
    return render(request, 'login/login.html', {'login_error': True})
