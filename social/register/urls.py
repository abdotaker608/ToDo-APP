from django.urls import path
from . import views

app_name = 'social'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('register/<str:error>/', views.register_error, name='register_error'),
    path('home/', views.home, name='home')
]