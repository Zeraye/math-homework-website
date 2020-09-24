from django.urls import path
from . import views

app_name = 'trigonometry'

urlpatterns = [
    path('', views.trigonometry, name='trigonometry')
]
