from django.urls import path
from . import views

app_name = 'login'

urlpatterns = [
    path('', views.login, name='login'),
    path('<str:login_error_404>/', views.login_error, name='login_error')
]