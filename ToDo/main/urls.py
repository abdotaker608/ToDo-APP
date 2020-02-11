from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('del/<int:item_id>/', views.delete, name='delete')
]