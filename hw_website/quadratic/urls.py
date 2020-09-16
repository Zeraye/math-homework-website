from django.urls import path
from . import views

app_name = 'quadratic'

urlpatterns = [
    path('', views.quadratic, name='quadratic')
]
